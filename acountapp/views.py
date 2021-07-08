from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def render_base(re):
    if re.method == 'POST' :
        return render(re, 'acountapp/hello_world.html',
                      context={"text" : "POST METHOD"})
    else:
        return render(re, 'acountapp/hello_world.html',
                      context={"text" : "GET METHOD"})

def render_test(re):
    return render(re, 'acountapp/hello_world_2.html')