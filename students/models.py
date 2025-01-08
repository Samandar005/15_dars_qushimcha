from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse
from courses.models import Course


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)
    slug = models.SlugField(unique=True)
    course = models.ManyToManyField(Course, related_name='students')
    notes = models.TextField()
    created_at = models.DateField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name)
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_detail_url(self):
        return reverse('students:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def get_update_url(self):
        return reverse('students:update', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def get_delete_url(self):
        return reverse('students:delete', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])