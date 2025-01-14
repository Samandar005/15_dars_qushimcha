# Generated by Django 5.1.4 on 2024-12-30 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=13)),
                ('slug', models.SlugField(unique=True)),
                ('notes', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('course', models.ManyToManyField(related_name='student_course', to='courses.course')),
            ],
        ),
    ]
