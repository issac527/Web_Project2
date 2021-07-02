from django.contrib import admin
from django.urls import path, include

from acountapp.views import render_base, render_test

app_name = 'acountapp'

urlpatterns = [
    path('rb/', render_base, name = "rb"),
    path('rt/', render_test, name = "rt")
]