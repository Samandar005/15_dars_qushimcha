from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'price', 'start_date', 'end_date', 'status')
    list_filter = ('status',)
    search_fields = ('course_name',)
    prepopulated_fields = {'slug': ('course_name',)}