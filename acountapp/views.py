from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from acountapp.models import HelloWorld


def render_base(re):
    if re.method == 'POST' :

        temp = re.POST.get("hwt")
        n_hw = HelloWorld()
        n_hw.text = temp
        n_hw.save()
        HelloWorld_list = HelloWorld.objects.all()

        return render(re, 'acountapp/hello_world.html',
                      context={"HelloWorld_list" : HelloWorld_list})
    else:
        HelloWorld_list = HelloWorld.objects.all()
        return render(re, 'acountapp/hello_world.html',
                      context={"HelloWorld_list" : HelloWorld_list})

def render_test(re):
    return render(re, 'acountapp/hello_world_2.html')