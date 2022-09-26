from django.conf import settings
from django.contrib.auth import get_user_model, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView


def main(request):
    return render(request, 'main.html')


class MainLoginView(LoginRequiredMixin, TemplateView):
    template_name = 'main_login.html'


main_login = MainLoginView.as_view()

user = get_user_model()


class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = settings.LOGIN_REDIRECT_URL
    template_name = 'signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        users = self.object
        auth_login(self.request, users)
        return response


signup = SignupView.as_view()


def signup_info(request):
    return render(request, 'signup_info.html')


def about_us(request):
    return render(request, 'about_us.html')


def recipe(request):
    return render(request, 'recipe.html')


def pinned_recipe(request):
    return render(request, 'pinned_recipe.html')
