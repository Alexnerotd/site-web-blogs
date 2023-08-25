from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .forms import MyUser, UseForm
from django.views.generic import ListView, CreateView, TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        return context


class UserListView(ListView):
    model = MyUser
    context_object_name = 'objects'
    template_name = 'perfil.html'

class UserRegisterView(CreateView):
    form_class = UseForm
    model = MyUser
    template_name = 'register.html'
    context_object_name = 'model'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.request.session['user_id'] = user.id
        return super().form_valid(form=form)


