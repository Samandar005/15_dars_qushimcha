from django.shortcuts import render, redirect, get_object_or_404
from .models import Course


def course_list(request):
    courses = Course.objects.all()
    ctx = {'courses': courses}
    return render(request, 'courses/course-list.html', ctx)

def course_create(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        description = request.POST.get('description')
        duration = request.POST.get('duration')
        price = request.POST.get('price')
        max_student = request.POST.get('max_student')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        if (
            course_name and description and duration and
                price and max_student and start_date
                and end_date
        ):
            Course.objects.create(
                course_name=course_name,
                description=description,
                duration=duration,
                price=price,
                max_student=max_student,
                start_date=start_date,
                end_date=end_date
            )
            return redirect('courses:list')
    return render(request, 'courses/course-create.html')

def course_detail(request, year, month, day, slug):
    course = get_object_or_404(
        Course,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )
    ctx = {'course': course}
    return render(request, 'courses/course-detail.html', ctx)

def course_delete(request, year, month, day, slug):
    course = get_object_or_404(
        Course,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )
    if request.method == 'POST':
        course.delete()
        return redirect('courses:list')
    ctx = {'course': course}
    return render(request, 'courses/course-delete-confirm.html', ctx)
