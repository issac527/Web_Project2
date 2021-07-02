from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def render_base(re):
    return render(re, 'acountapp/hello_world.html')

def render_test(re):
    return render(re, 'acountapp/hello_world_2.html')