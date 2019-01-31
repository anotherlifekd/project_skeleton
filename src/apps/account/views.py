from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from apps.account.tasks import task_number_one


def index(request):
    task_number_one.delay()
    return HttpResponse('YES')
