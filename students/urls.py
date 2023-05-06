from django.urls import path
from students.views import  landing, get_students, students_index, students_info
urlpatterns = [

    path('',landing, name='students.landing'),
    path('all', get_students, name='students.all'),
    path('index' , students_index, name='students.index'),
    path('<int:id>', students_info, name='student.show')

]
