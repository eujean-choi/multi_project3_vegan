from django.contrib import admin
from .models import UserInfo, RecipeIngredient, Recipe, Rating, PinnedRecipe, IngredientPrice, IngredientCode

admin.site.register(RecipeIngredient)
admin.site.register(Recipe)
admin.site.register(Rating)
admin.site.register(PinnedRecipe)
admin.site.register(IngredientPrice)
admin.site.register(IngredientCode)

@admin.register(UserInfo)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_name', 'user_pw', 'email',
                    'age', 'gender', 'height', 'weight']
