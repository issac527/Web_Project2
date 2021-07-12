from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from django.views.generic import CreateView

# Create your views here.
from acountapp.models import HelloWorld
from django.urls import reverse, reverse_lazy

def render_base(re):
    if re.method == 'POST' :

        temp = re.POST.get("hwt")
        n_hw = HelloWorld()
        n_hw.text = temp
        n_hw.save()

        return HttpResponseRedirect(reverse("acountapp:rb"))
    else:
        HelloWorld_list = HelloWorld.objects.all()
        return render(re, 'acountapp/hello_world.html',
                      context={"HelloWorld_list" : HelloWorld_list})

def render_test(re):
    return render(re, 'acountapp/hello_world_2.html')

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # 클래스 내에서 reverse시 reverse_lazy로 사용
    success_url = reverse_lazy("acountapp:create")
    template_name = "acountapp/create.html"