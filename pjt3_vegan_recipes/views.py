from django.conf import settings
from django.contrib.auth import get_user_model, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView


def main(request):
    return render(request, 'main.html')

def main_login(request):
    return render(request, 'main_login.html')

# def signup(request):
#     return render(request, 'signup.html')

user = get_user_model()

class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = settings.LOGIN_REDIRECT_URL
    template_name = 'signup.html'
    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        auth_login(self.request, user)
        return response

signup = SignupView.as_view()

def signup_2(request):
    return render(request, 'signup_2.html')


def about_us(request):
    return render(request, 'about_us.html')

def recipe(request):
    return render(request, 'recipe.html')

def pinned_recipe(request):
    return render(request, 'pinned_recipe.html')
