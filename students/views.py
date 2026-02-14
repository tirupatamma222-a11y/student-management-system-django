from django.shortcuts import render
from django.shortcuts import redirect
from .models import Student
# Create your views here.


def student_form(request):
    message = ""
    if request.method == "POST":
        Student.objects.create(
            name = request.POST['name'],
            roll_number = request.POST['roll'],
            student_class = request.POST['class'],
            age = request.POST['age'],
            parent_contact = request.POST['contact']

        )
        message = "student added sucessfully!"
    return render(request,'student_form.html',{'message':message})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def student_update(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.roll_number = request.POST['roll']
        student.student_class = request.POST['class']
        student.age = request.POST['age']
        student.parent_contact = request.POST['contact']
        student.save()
        return redirect('/students/list/')

    return render(request, 'student_update.html', {'student': student})


def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/students/list/')