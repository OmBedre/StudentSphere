# Generated by Django 5.0.7 on 2024-08-05 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_seesion_year_session_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seesion_year',
            name='session_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='seesion_year',
            name='session_start',
            field=models.DateField(),
        ),
    ]