from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.utils.decorators import method_decorator

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

# Create your views here.
from django.views.generic.list import MultipleObjectMixin

from acountapp.decorators import account_ownership_required
from acountapp.forms import AccountCreationForm
from acountapp.models import HelloWorld
from django.urls import reverse, reverse_lazy

from articleapp.models import Article

has_list = [login_required, account_ownership_required]

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # 클래스 내에서 reverse시 reverse_lazy로 사용
    #success_url = reverse_lazy("acountapp:create")
    template_name = "acountapp/create.html"
    def get_success_url(self):
        return reverse("acountapp:detail", kwargs={'pk': self.object.pk})


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = "acountapp/detail.html"

    paginate_by = 20

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object)
        return super().get_context_data(object_list=article_list, **kwargs)


@method_decorator(has_list, 'get')
@method_decorator(has_list, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    #success_url = reverse_lazy('acountapp:rb')
    template_name = "acountapp/update.html"
    def get_success_url(self):
        return reverse("acountapp:detail", kwargs={'pk': self.object.pk})


@method_decorator(has_list, 'get')
@method_decorator(has_list, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('articleapp:list')
    template_name = "acountapp/delete.html"
