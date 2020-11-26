from django.shortcuts import render
from .models import Homework, Lesson


def home_page(request):
    return render(request, 'home_page/main.html')

def homework(request, slug):
    homeworks = Homework.objects.all()

    return render(request, 'home_page/homework.html', {"homeworks": homeworks})