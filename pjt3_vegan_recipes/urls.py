"""pjt3_vegan_recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('main_login/', views.main_login, name='main_login'),
    path('recipe/', views.recipe, name='recipe'),
    path('signup/', views.signup, name='signup'),
    path('signup_info/', views.signup_info, name='signup_info'),
    path('signup_recipe/', views.signup_recipe, name='signup_recipe'),
    #path('signup_2/', views.signup_2, name='signup_2'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #path('profile/', views.profile, name='profile'),
    # path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('pinned_recipe/', views.pinned_recipe, name='pinned_recipe'),
    # path('about_us/', views.about_us, name='about_us'),
]
