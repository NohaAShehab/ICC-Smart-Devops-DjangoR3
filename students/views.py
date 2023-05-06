from django.shortcuts import render
from django.http import HttpResponse
from  students.models import Student

# Create your views here.

def landing(request):
    # return HttpResponse("---students landing page ---- ")
    return render(request, 'students/landing.html')


students = ['Ahmed', 'Mohamed', "Mariam", "Merit",
            'Andrew', 'AbdAllah']


def get_students(request):
    return render(request, 'students/students.html', context={"students": students})


def students_index(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', context={"students": students})


def students_info(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'students/show.html', context={"student": student})