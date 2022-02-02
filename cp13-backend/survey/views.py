import csv

from django.db import connection
from django.db.models import Count
from django.http import HttpResponse
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.exceptions import NotFound, NotAcceptable
from rest_framework.response import Response
from surveytaker.models import Response as SurveyResponse
from surveybuilder.models import Survey, Block, Question, TextboxQuestionDecimal
from django.db import models
from surveybuilder.views import survey_data, questionTypeModel


@api_view(['GET'])
# @permission_classes([IsAuthenticated, ])
def test_view(request, survey_id):
    try:
        survey = Survey.objects.get(id=survey_id)
    except models.ObjectDoesNotExist:
        raise NotFound(detail="Survey not found!", code=None)
    with connection.cursor() as cursor:
        cursor.execute("select * from surveybuilder_survey where id = %s", (survey_id,))
        row = cursor.fetchall()
        response = HttpResponse(
            content_type='text/csv',
            headers={
                'Content-Disposition': f'attachment; filename="{survey.name} {survey.language} Version Response (ID {survey.id}).csv"'},
        )
        writer = csv.writer(response)
        survey_responses = SurveyResponse.objects.filter(survey_id=survey_id)
        writer.writerow(["response_id", "question_id", "create_date", "contact_info", "content", "identifier"])
        for el in survey_responses:
            writer.writerow([el.id, el.question_id, el.create_date, el.contact_info, el.content, el.identifier])
    return response


@api_view(['GET'])
# @permission_classes([IsAuthenticated, ])
def metadata_info_view(request, survey_id):
    try:
        survey = Survey.objects.get(id=survey_id)
    except models.ObjectDoesNotExist:
        raise NotFound(detail="Survey not found!", code=None)
    survey_responses = SurveyResponse.objects.filter(survey_id=survey_id)
    if len(survey_responses) == 0:
        res = {
            "last_response_time": None,
            "total_responses": None,
        }
    else:
        res = {
            "last_response_time": survey_responses.order_by("-create_date")[0].create_date,
            "total_responses": survey_responses.values("identifier").distinct().count(),
        }
    return Response(res)


@api_view(["GET"])
def export_survey(request, survey_id):
    # fetch survey title, id, language
    try:
        survey = Survey.objects.get(id=survey_id)
    except models.ObjectDoesNotExist:
        raise NotFound(detail="Survey not found!", code=None)
    config_json = survey_data(request._request, survey_id)

    response = HttpResponse(
        config_json,
        content_type='application/json',
        headers={
            'Content-Disposition': f'attachment; filename="{survey.name} {survey.language} Version Configuration (ID {survey.id}).json"'},
    )
    return response


@api_view(["GET"])
def response_day(request, survey_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT identifier, max(create_date), count(*) FROM surveytaker_response  WHERE survey_id = %s GROUP BY identifier", [survey_id])
        rows = cursor.fetchall()
    
    return Response(rows)

@api_view(["POST"])
def import_survey(request):
    try:
        # fetch survey title, id, language
        data = request.data
        print(data)
        survey = Survey()
        if 'name' in data:
            survey.name = data['name']
        if 'language' in data:
            survey.language = data['language']
        if 'consentText' in data:
            survey.consentText = data['consentText']
        if 'timelimitMinutes' in data:
            survey.timelimitMinutes = data['timelimitMinutes']
        if 'active' in data:
            survey.active = data['active']

        survey.save()

        if 'blocks' in data:
            for block in data['blocks']:
                b = Block()
                b.survey = survey
                if 'title' in block:
                    b.title = block['title']
                if 'description' in block:
                    b.description = block['description']
                if 'order' in block:
                    b.order = block['order']
                b.save()

                if 'questions' in block:
                    for question in block['questions']:
                        q = Question()
                        q.block = b
                        if 'name' in question:
                            q.name = question['name']
                        if 'type' in question:
                            q.type = question['type']
                        if 'description' in question:
                            q.description = question['description']
                        if 'required' in question:
                            q.required = question['required']
                        if 'order' in question:
                            q.order = question['order']
                        q.save()

                        typedata = question['typedata']
                        # del typedata['id']
                        # del typedata['question']

                        datatype = questionTypeModel[q.type](**question['typedata'])
                        datatype.question = q
                        datatype.save()

        return Response({"status": "success"})
    except Exception:
        raise NotAcceptable(detail="Survey cannot be imported!")


