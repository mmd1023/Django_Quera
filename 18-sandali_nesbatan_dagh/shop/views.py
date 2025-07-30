from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import PersonalInformation
from .models import Person
from django.http import HttpResponse


@csrf_exempt
def personal_page(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        context = {
            'persons': persons
        }
        return render(request, 'main.html', context)

    elif request.method == 'POST':
        form = PersonalInformation(request.POST)

        if not form.is_valid():
            return HttpResponse("Error", status=400)
        
        person = Person.objects.create(
            full_name = form.cleaned_data['full_name'],
            height = form.cleaned_data['height'],
            age = form.cleaned_data['age'],
            gender = form.cleaned_data['gender']
        )

        return HttpResponse(person, status=201)

