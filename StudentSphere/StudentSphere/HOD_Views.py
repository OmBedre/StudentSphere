from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from app.models import Course, Session_Year, CustomUser, Student, Staff, Subject
from django.contrib import messages


@login_required(login_url='/')
def home(request):
    return render(request, 'HOD/home.html')


@login_required(login_url='/')
def VIEW_STUDENTS(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'HOD/Student/view_student.html', context)


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
                user_type='3'
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
            messages.success(request, user.first_name + " " + user.last_name + "Successfully Created")
            return redirect('add_students')

    context = {
        'courses': courses,
        'session_years': session_years
    }
    return render(request, 'HOD/Student/add_student.html', context)


@login_required(login_url='/')
def EDIT_STUDENTS(request, id):
    student = get_object_or_404(Student, id=id)
    courses = Course.objects.all()
    session_years = Session_Year.objects.all()
    context = {
        'student': student,
        'courses': courses,
        'session_years': session_years,
    }

    return render(request, 'HOD/Student/edit_student.html', context)


@login_required(login_url='/')
def UPDATE_STUDENTS(request):
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
        student_id = request.POST.get('student_id')

        user = CustomUser.objects.get(id=student_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != "" and password is not None:
            user.set_password(password)

        if profile_pic != "" and profile_pic is not None:
            user.profile_pic = profile_pic
        user.save()

        student = Student.objects.get(admin=student_id)
        student.address = address
        student.gender = gender

        course = Course.objects.get(id=course_id)
        student.course_id = course

        session_year = Session_Year.objects.get(id=session_year_id)
        student.session_year_id = session_year

        student.save()
        messages.success(request, 'Record successfully updated')
        return redirect('view_students')
    return render(request, 'HOD/Student/edit_student.html')


@login_required(login_url='/')
def DELETE_STUDENTS(request, admin):
    student = CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request, 'Record successfully deleted')
    return redirect('view_students')


@login_required(login_url='/')
def ADD_COURSES(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')

        course = Course(
            name=course_name,
        )
        course.save()
        messages.success(request, 'Course is Successfully created')
        return redirect('add_courses')

    return render(request, 'HOD/Course/add_course.html')


@login_required(login_url='/')
def VIEW_COURSES(request):
    course = Course.objects.all()
    context = {
        'course': course,
    }
    return render(request, 'HOD/Course/view_course.html', context)


@login_required(login_url='/')
def EDIT_COURSE(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course': course,
    }
    return render(request, 'HOD/Course/edit_course.html', context)


@login_required(login_url='/')
def UPDATE_COURSE(request):
    if request.method == "POST":
        name = request.POST.get('course_name')
        course_id = request.POST.get('course_id')

        course = Course.objects.get(id=course_id)
        course.name = name
        course.save()
        messages.success(request, 'Course Successfully Updated')
        return redirect('view_courses')

    return render(request, 'HOD/Course/edit_course.html')


@login_required(login_url='/')
def DELETE_COURSE(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, 'Course is Successfully Deleted')
    return redirect('view_courses')


@login_required(login_url='/')
def VIEW_STAFF(request):
    staff = Staff.objects.all()

    context = {
        'staff': staff
    }
    return render(request, 'HOD/Staff/view_staff.html', context)


@login_required(login_url='/')
def ADD_STAFF(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already taken!')
            return redirect('add_staff')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is already taken!')
            return redirect('add_staff')

        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                profile_pic=profile_pic,
                user_type=2,
            )
            user.set_password(password)
            user.save()

            staff = Staff(
                admin=user,
                address=address,
                gender=gender,

            )
            staff.save()

            messages.success(request, f'{user.username} has been successfully created as Staff Profile.')
            return redirect('add_staff')

    return render(request, 'HOD/Staff/add_staff.html')


@login_required(login_url='/')
def EDIT_STAFF(request, id):
    staff = Staff.objects.get(id=id)
    context = {
        'staff': staff,
    }
    return render(request, 'Hod/Staff/edit_staff.html', context)


@login_required(login_url='/')
def DELETE_STAFF(request, admin):
    staff = CustomUser.objects.get(id=admin)

    staff.delete()
    messages.success(request, 'Successfully Deleted the Record !!')
    return redirect('view_staff')


@login_required(login_url='/')
def UPDATE_STAFF(request, id):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        staff_id = request.POST.get('staff_id')

        user = CustomUser.objects.get(id=staff_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        if profile_pic != "" and profile_pic is not None:
            user.profile_pic = profile_pic
        if password != "" and password is not None:
            user.set_password = password
        user.save()

        staff = Staff.objects.get(admin=staff_id)
        staff.gender = gender
        staff.address = address
        staff.save()
        messages.success(request, 'Staff is Successfully Updated!!')

        return redirect('view_staff')


@login_required(login_url='/')
def EDIT_SUBJECT(request, id):
    subject = Subject.objects.get(id=id)
    staff = Staff.objects.all()
    course = Course.objects.all()

    context = {
        'subject': subject,
        'staff': staff,
        'course': course,
    }
    return render(request, 'HOD/Subjects/edit_subject.html', context)


@login_required(login_url='/')
def UPDATE_SUBJECT(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')
        subject_name = request.POST.get('subject_name')

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject(
            id = subject_id,
            name = subject_name,
            course=course,
            staff=staff,
        )
        subject.save()
        messages.success(request,'Subject is Successfully Updated')
        return redirect('view_subject')


@login_required(login_url='/')
def VIEW_SUBJECT(request):
    subject = Subject.objects.all()
    context = {
        'subject': subject,
    }
    return render(request, 'HOD/Subjects/view_subject.html', context)


@login_required(login_url='/')
def ADD_SUBJECT(request):
    course = Course.objects.all()
    staff = Staff.objects.all()

    if request.method == "POST":
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject(
            name=subject_name,
            course=course,
            staff=staff,
        )
        subject.save()
        messages.success(request, '{{subject_name}} are Successfully Added!!')
        return redirect('view_subject')

    context = {
        'course': course,
        'staff': staff,
    }
    return render(request, 'HOD/Subjects/add_subject.html', context)


@login_required(login_url='/')
def DELETE_SUBJECT(request, id):
    subject = Subject.objects.filter(id=id)
    subject.delete()
    messages.success(request,'Subject is Successfully Deleted...')
    return redirect('view_subject')
