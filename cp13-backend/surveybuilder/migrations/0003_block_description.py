# Generated by Django 3.2.7 on 2021-09-29 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveybuilder', '0002_auto_20210911_0716'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='description',
            field=models.CharField(default='', max_length=15000),
        ),
    ]