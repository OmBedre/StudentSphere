from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from app.models import Course, Session_Year


@login_required(login_url='/')
def home(request):
    return render(request, 'HOD/home.html')


def VIEW_STUDENTS(request):
    return render(request, 'HOD/view_student.html')


def ADD_STUDENTS(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    context = {
        'course': course,
        'session_year': session_year
    }
    return render(request, 'HOD/add_student.html', context)
