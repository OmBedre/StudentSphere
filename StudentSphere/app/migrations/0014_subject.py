# Generated by Django 5.0.7 on 2024-10-20 21:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='app.course')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_subjects', to='app.staff')),
            ],
        ),
    ]
