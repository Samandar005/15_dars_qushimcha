# Generated by Django 5.1.4 on 2025-01-09 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('completed', 'Completed'), ('in_progress', 'In Progress'), ('passed', 'Passed')], default='in_progress', max_length=11),
        ),
    ]
