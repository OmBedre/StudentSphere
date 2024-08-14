from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from app.models import Course, Session_Year, CustomUser, Student
from django.contrib import messages


@login_required(login_url='/')
def home(request):
    return render(request, 'HOD/home.html')


def VIEW_STUDENTS(request):
    return render(request, 'HOD/view_student.html')


@login_required(login_url='/')
def ADD_STUDENTS(request):
    courses = Course.objects.all()
    session_years = Session_Year.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        address = request.POST.get('address')

        if not course_id or not session_year_id:
            messages.error(request, 'Please select both a course and a session year')
            return redirect('add_students')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already registered')
            return redirect('add_students')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is already registered')
            return redirect('add_students')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type='3'  # Set user type to 'STUDENT'
            )
            user.set_password(password)
            user.save()

            try:
                course = Course.objects.get(id=course_id)
                session_year = Session_Year.objects.get(id=session_year_id)
            except Course.DoesNotExist:
                messages.error(request, 'Selected course does not exist')
                return redirect('add_students')
            except Session_Year.DoesNotExist:
                messages.error(request, 'Selected session year does not exist')
                return redirect('add_students')

            # Create Student object with correct field names
            student = Student(
                admin=user,
                address=address,
                session_year_id=session_year,  # Use session_year_id
                course_id=course,  # Use course_id
                gender=gender
            )
            student.save()
            messages.success(request, user.first_name + " " + user.last_name+"Successfully Created")
            return redirect('add_students')

    context = {
        'courses': courses,
        'session_years': session_years
    }
    return render(request, 'HOD/add_student.html', context)


