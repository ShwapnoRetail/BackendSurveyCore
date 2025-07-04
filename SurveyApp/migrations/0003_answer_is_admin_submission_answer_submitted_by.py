# Generated by Django 5.2.1 on 2025-06-16 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SurveyApp', '0002_remove_answer_location_lat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='is_admin_submission',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='answer',
            name='submitted_by',
            field=models.JSONField(default=dict),
        ),
    ]
