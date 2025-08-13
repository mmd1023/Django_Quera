from django.shortcuts import HttpResponse
from .models import Musician
from django.views import View


class Musician_list(View):
    def get(self, request):
        musician_list = Musician.objects.order_by('name').values_list('name', flat=True)
        return HttpResponse(musician_list)