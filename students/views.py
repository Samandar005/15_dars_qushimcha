from django.shortcuts import render, redirect, get_object_or_404

from courses.models import Course
from students.models import Student


def home(request):
    return render(request, 'index.html')

def student_list(request):
    students = Student.objects.all()
    selected_courses = []

    if request.method == "POST":
        selected_courses = request.POST.getlist("courses")

    ctx = {'students': students,
           'selected_courses': selected_courses}
    return render(request, 'students/student-list.html', ctx)


def student_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        course = request.POST.getlist('courses')
        notes = request.POST.get('notes')
        print(first_name, last_name, email, phone_number, course, notes)

        if (
                first_name and last_name and email and
                phone_number and course and notes
        ):
            student = Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                notes=notes
            )
            for course_id in course:
                course = Course.objects.get(pk=course_id)
                student.course.add(course)

            return redirect('students:list')

    courses = Course.objects.all()
    ctx = {'courses': courses}
    return render(request, 'students/student-create.html', ctx)


def student_detail(request, year, month, day, slug):
    student = get_object_or_404(
        Student,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )
    courses = Course.objects.all()
    ctx = {'student': student, 'courses': courses}
    return render(request, 'students/student-detail.html', ctx)

def student_delete(request, year, month, day, slug):
    student = get_object_or_404(
        Student,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )
    if request.method == 'POST':
        student.delete()
        return redirect('students:list')
    ctx = {'student': student}
    return render(request, 'students/student-delete-confirm.html', ctx)


def student_update(request, year, month, day, slug):
    student = get_object_or_404(
        Student,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )

    selected_courses = student.course.values_list('id', flat=True)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        courses = request.POST.getlist('courses')  # multiple uchun getlist
        notes = request.POST.get('notes')

        # Ma'lumotlarni tekshirish
        if (
                first_name and last_name and email and
                phone_number and courses and notes
        ):
            student.first_name = first_name
            student.last_name = last_name
            student.email = email
            student.phone_number = phone_number
            student.notes = notes

            # Kurslarni yangilash
            student.course.set(courses)  # yangi kurslarni qo'shish

            student.save()
            # Muvaffaqiyatli yangilanganidan so'ng, foydalanuvchini ma'lum qiling

            return redirect(student.get_detail_url())

    ctx = {
        'student': student,
        'courses': Course.objects.all(),  # Barcha kurslarni olish
        'selected_courses': selected_courses  # Tanlangan kurslarni olish
    }

    return render(request, 'students/student-create.html', ctx)