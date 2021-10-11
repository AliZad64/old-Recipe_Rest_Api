from django.contrib import admin
from .models import Recipe , Ingrident, RecipeType , Species, Test
# Register your models here.

admin.site.register(Recipe)
admin.site.register(Ingrident)
admin.site.register(Species)

admin.site.register(RecipeType)
admin.site.register(Test)