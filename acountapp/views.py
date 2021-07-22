from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.utils.decorators import method_decorator

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

# Create your views here.
from acountapp.decorators import account_ownership_required
from acountapp.forms import AccountCreationForm
from acountapp.models import HelloWorld
from django.urls import reverse, reverse_lazy

has_list = [login_required, account_ownership_required]


@login_required(login_url=reverse_lazy('acountapp:login'))
def render_base(re):
    # 요청을 보내는 유저가 로그인이 되어있다면 아래 구문 실행
    if re.user.is_authenticated:

        if re.method == 'POST':

            temp = re.POST.get("hwt")
            n_hw = HelloWorld()
            n_hw.text = temp
            n_hw.save()

            return HttpResponseRedirect(reverse("acountapp:rb"))
        else:
            HelloWorld_list = HelloWorld.objects.all()
            return render(re, 'acountapp/hello_world.html',
                          context={"HelloWorld_list": HelloWorld_list})
    else:
        return HttpResponseRedirect(reverse("acountapp:login"))


def render_test(re):
    return render(re, 'acountapp/hello_world_2.html')


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # 클래스 내에서 reverse시 reverse_lazy로 사용
    success_url = reverse_lazy("acountapp:create")
    template_name = "acountapp/create.html"


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = "acountapp/detail.html"


@method_decorator(has_list, 'get')
@method_decorator(has_list, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('acountapp:rb')
    template_name = "acountapp/update.html"


@method_decorator(has_list, 'get')
@method_decorator(has_list, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('acountapp:rb')
    template_name = "acountapp/delete.html"
