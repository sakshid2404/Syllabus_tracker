<<<<<<< HEAD
from django.contrib.auth import login, logout
from django.views.generic import FormView, View
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import RegisterForm, LoginForm


class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('syllabus-list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('syllabus-list')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect(self.get_success_url())



class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
=======
>>>>>>> 3d75138126cb3fff9bad839173cb6795ce19e372
