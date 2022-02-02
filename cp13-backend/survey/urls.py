from django.urls import path

from survey.views import test_view, export_survey, metadata_info_view, import_survey, response_day

urlpatterns = [
    path('response/<int:survey_id>/', test_view),
    path('export/<int:survey_id>/', export_survey),
    path('import/', import_survey),
    path('metadata_info/<int:survey_id>/', metadata_info_view),
    path('response_day/<int:survey_id>/', response_day),
]
