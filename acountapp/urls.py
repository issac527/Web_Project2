from django.contrib import admin
from django.urls import path, include

from acountapp.views import MYH_print

app_name = 'acountapp'

urlpatterns = [
    path('mp/', MYH_print, name = "mp")
]