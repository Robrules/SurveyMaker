# Generated by Django 3.2.7 on 2021-11-12 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveybuilder', '0015_auto_20211102_0439'),
    ]

    operations = [
        migrations.AddField(
            model_name='buttonquestion',
            name='goToEnd',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='buttonrowquestion',
            name='goToEnd',
            field=models.BooleanField(default=False),
        ),
    ]