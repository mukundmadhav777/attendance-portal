from django.shortcuts import render
from testapp.models import Portal
from testapp.forms import attendance

def student_attendance(request):
    form=attendance()
    if request.method=='POST':
        form=attendance(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'testapp/attendance.html',{'form':form})
def view_attendance(request):
    attendance_list=Portal.objects.all()
    return render(request,'testapp/view.html',{'attendance_list':attendance_list})
