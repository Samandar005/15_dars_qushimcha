# Generated by Django 5.1.4 on 2025-01-07 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('Completed', 'completed'), ('In Progress', 'in_progress'), ('Passed', 'passed')], default='in_progress', max_length=11),
        ),
    ]
