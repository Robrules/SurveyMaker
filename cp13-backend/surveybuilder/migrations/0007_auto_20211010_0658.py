# Generated by Django 3.2.7 on 2021-10-10 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveybuilder', '0006_remove_choice_uniquechoice'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choice',
            new_name='MultiChoice',
        ),
        migrations.AlterField(
            model_name='multichoice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveybuilder.multichoicequestion'),
        ),
    ]
