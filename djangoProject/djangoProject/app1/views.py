from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app1.models import Student


def first_page(request):
    student_list = Student.objects.all()
    student_str = map(str, student_list)
    return HttpResponse("<p>app1【" + ''.join(student_str) + "】</p>")
