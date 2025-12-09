from django.http import HttpResponse

def happy(req, name, times):
    return HttpResponse(f'You are great, {name} :)<br>' * times)

def sad(req, name):
    return HttpResponse(f'Nobody likes you, {name}!')