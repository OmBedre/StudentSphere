# Generated by Django 5.0.7 on 2024-08-14 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_seesion_year_session_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('1', 'HOD'), ('2', 'STAFF'), ('3', 'STUDENT')], default='1', max_length=50),
        ),
    ]