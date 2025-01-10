from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse


class Course(models.Model):

    STATUS_CHOICES = (
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('passed', 'Passed')
    )

    course_name = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    max_student = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    slug = models.SlugField(unique=True)
    created_at = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default='in_progress')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.course_name)
        super(Course, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('courses:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def get_delete_url(self):
        return reverse('courses:delete', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])