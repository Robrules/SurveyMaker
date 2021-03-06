# Generated by Django 3.2.7 on 2021-11-10 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveybuilder', '0015_auto_20211102_0439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Randomiser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subset', models.IntegerField(default=None)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveybuilder.survey')),
            ],
        ),
        migrations.AddField(
            model_name='block',
            name='randomiser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveybuilder.randomiser'),
        ),
    ]
