# Generated by Django 5.0.7 on 2024-08-05 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_seesion_year_session_end_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Seesion_Year',
            new_name='Session_Year',
        ),
    ]