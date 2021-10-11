from food.schemas.ingridents_schema import testOut
from os import name
from ninja import Router
from food.schemas.recipes_schemas import AutoRecipesOut, RecipeIn , RecipeOut , AutoRecipesOut , AutoRecipesIn , RecipeSchema
from food.schemas.junction_schema import testOut
from food.models import Test, Recipe , Ingrident
from typing import List

recipes_controller = Router(tags=["recipes"])

@recipes_controller.get("/retreiveall", response=List[RecipeOut])
def recipes_all(request):
    return Recipe.objects.all()

@recipes_controller.get("/retreive/{recipe_id}", response= RecipeOut)
def recipes_get(request , recipe_id:int):
    recipe = Recipe.objects.get(id = recipe_id)
    return recipe

@recipes_controller.post("/create" , response=RecipeOut)
def recipes_post(request , payload: RecipeIn):
    recipelol = Recipe(name=payload.name, photo=payload.photo, duration=payload.duration)
    recipelol.save()
    recipelol.recipe_ingrident.add(*payload.recipe_ingrident)
    return recipelol

@recipes_controller.get("/getbyingrident", response=RecipeOut)
def recipe_filter(request, payload: RecipeIn):
    recipe = Recipe.objects.filter()