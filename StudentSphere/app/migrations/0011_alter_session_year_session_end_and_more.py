# Generated by Django 5.0.7 on 2024-08-17 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_course_name_alter_session_year_session_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session_year',
            name='session_end',
            field=models.CharField(max_length=105),
        ),
        migrations.AlterField(
            model_name='session_year',
            name='session_start',
            field=models.CharField(max_length=105),
        ),
    ]