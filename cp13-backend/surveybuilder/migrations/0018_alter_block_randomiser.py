# Generated by Django 3.2.7 on 2021-11-11 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveybuilder', '0017_auto_20211111_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='randomiser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='surveybuilder.randomiser'),
        ),
    ]
