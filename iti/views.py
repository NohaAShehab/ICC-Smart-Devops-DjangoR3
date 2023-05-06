from django.shortcuts import render
from django.http import  HttpResponse
from django.http import HttpResponseNotFound

# Create your views here.


## handle http request
def helloworld(request):
    return HttpResponse("<h1> Hello  world </h1> ")


###
courses = ['django', 'ansible', 'docker', 'git']

def get_courses(request):
    return HttpResponse(courses)


def get_specific_course(request, index):
    print(index, type(index))
    index = int(index)
    if index in range(len(courses)):
        return HttpResponse(f"<h1> course={courses[index]} </h1>")

    return HttpResponseNotFound("<h1>course not found </h1>")


