from django.conf import settings
from django.contrib.auth import get_user_model, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView
from .models import *
from datetime import datetime, timedelta
# from .Recommender_Systems import *

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


def signup_recipe(request):
    return render(request, 'signup_recipe.html')


def about_us(request):
    return render(request, 'about_us.html')


def recipe(request, id):

    recipe_one = Recipe.objects.get(recipe_id=id)

    # 재료 덩어리 리스트로 만들기 #
    ingredients = recipe_one.ingredients
    ingredients = ingredients.split('[')[1]
    ingredients = ingredients.split(']')[0]
    ingredient_list = list()
    ingredient_list = ingredients.split(',')

    # 레시피 덩어리 리스트로 만들기 #
    recipe_bulk = recipe_one.recipe
    recipe_bulk = recipe_bulk.split('[')[1]
    recipe_bulk = recipe_bulk.split(']')[0]
    recipe_tmplist = list()
    # 레시피 방법 순으로 자르기 ('"' 기준으로 구분 > 홀수 요소만 추출)
    recipe_tmplist = recipe_bulk.split('"')
    recipe_tmplist = recipe_tmplist[1::2]
    # 숫자 표시 지우고 리스트에 담기
    recipe_list = list()
    for recipe_item in recipe_tmplist:
        point = recipe_item.index('.')
        recipe_item = recipe_item[(point+2):]
        recipe_list.append(recipe_item)

    return render(request, 'recipe.html', {'list': recipe_one, 'ingredient_list': ingredient_list, 'recipe_list': recipe_list})


def pinned_recipe(request):

    today = datetime.today().strftime('%Y-%m-%d')
    yesterday_get = datetime.today() - timedelta(days=1)
    yesterday = yesterday_get.strftime('%Y-%m-%d')

    pinned_all = PinnedRecipe.objects.select_related('recipe')

    for data in pinned_all:
        print(data.date)


    return render(request, 'pinned_recipe.html', {'list': pinned_all})

def search_result(request):

    # sqlalchemy로 연결
    # df = Download_dataset('recipe')
    # print(df)

    # # models.py로 연결
    # queryset = Recipe.objects.all()
    # query, params = queryset.query.sql_with_params()
    # df = pd.read_sql_query(query, connections['default'], params=params)
    # print(df)


    return render(request, 'search_result.html')

def Make_dummy(request):
    return render(request, 'search_result.html')
