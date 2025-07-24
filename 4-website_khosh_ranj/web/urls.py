from django.urls import path

from .views import *

urlpatterns = [
    path('happy/<str:name>/<int:times>/', happy),
    path('sad/<str:name>/', sad),
]
