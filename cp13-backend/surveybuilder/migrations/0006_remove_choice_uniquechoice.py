# Generated by Django 3.2.7 on 2021-10-10 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveybuilder', '0005_alter_multichoicequestion_options'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='choice',
            name='UniqueChoice',
        ),
    ]
