# Generated by Django 3.2.7 on 2021-10-24 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveybuilder', '0008_textboxquestiontext_validate'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='LikertScaleQuestion',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('numberRows', models.IntegerField(default=None)),
        #         ('numberColumns', models.IntegerField(default=None)),
        #         ('entry', models.CharField(default='', max_length=500)),
        #         ('minTitle', models.CharField(default='', max_length=5000)),
        #         ('middleTitle', models.CharField(default='', max_length=5000)),
        #         ('maxTitle', models.CharField(default='', max_length=5000)),
        #         ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveybuilder.question')),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='LikertChoice',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('order', models.IntegerField(default=None)),
        #         ('title', models.CharField(default='', max_length=5000)),
        #         ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveybuilder.likertscalequestion')),
        #     ],
        # ),
        migrations.CreateModel(
            name='DragAndDropQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.IntegerField(default=0)),
                ('textboxMax', models.IntegerField(default=1)),
                ('textboxMin', models.IntegerField(default=1)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveybuilder.question')),
            ],
        ),
        migrations.CreateModel(
            name='DragAndDropChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=None)),
                ('title', models.CharField(default='', max_length=5000)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveybuilder.draganddropquestion')),
            ],
        ),
    ]