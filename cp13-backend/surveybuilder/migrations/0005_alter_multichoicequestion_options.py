# Generated by Django 3.2.7 on 2021-10-10 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveybuilder', '0004_auto_20210929_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multichoicequestion',
            name='options',
            field=models.IntegerField(default=0),
        ),
    ]
