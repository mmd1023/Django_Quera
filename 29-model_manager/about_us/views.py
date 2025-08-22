from django.shortcuts import render
from django.contrib.auth import get_user_model


def about_us(request):
    User = get_user_model()
    return render(request, 'about_us.html', {'users': User.objects.all()})
