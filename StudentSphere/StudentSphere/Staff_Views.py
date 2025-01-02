from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render

from app.models import Staff, Staff_Notification, Staff_Leave


@login_required(login_url='/')
def HOME(request):
    return render(request, 'Staff/home.html')


@login_required(login_url='/')
def NOTIFICATIONS(request):
    try:
        staff = Staff.objects.get(admin=request.user)
        notifications = Staff_Notification.objects.filter(staff_id=staff)
        return render(request, 'Staff/Notifications.html', {'messages': notifications})
    except Staff.DoesNotExist:
        messages.error(request, "You are not authorized to view this page.")
        return redirect('home')


@login_required(login_url='/')
def Mark_as_Done(request, status):
    notification = Staff_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect("staff_notifications")


@login_required(login_url='/')
def LEAVE_APPLICATION(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id
        staff_leave_history = Staff_Leave.objects.filter(staff_id=staff_id)
        context = {
            'staff_leave_history': staff_leave_history,
        }
        return render(request, 'Staff/Leave_Application.html', context)


@login_required(login_url='/')
def LEAVE_APPLY_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        staff_id = Staff.objects.get(admin=request.user.id)

        leave = Staff_Leave(
            staff_id=staff_id,
            data=leave_date,
            message=leave_message,
        )
        leave.save()
        messages.success(request, 'Leave Applied Successfully')
        return redirect('staff_apply_leave')
