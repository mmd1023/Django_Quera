from .models import Task
from django.http import HttpResponse


def list_create_tasks(request):
    if request.method == 'GET':
        return HttpResponse('\n'.join(Task.objects.order_by('name').values_list('name', flat=True)))


def count_tasks(request):
    if request.method == 'GET':
        return  HttpResponse(f'You have \'{Task.objects.count()}\' tasks to do')
