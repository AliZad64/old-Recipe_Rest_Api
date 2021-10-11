from food.models import Ingrident, Recipe
from ninja import  Schema
from food.schemas.ingridents_schema import ingridentOut , ingridentAutoOut, ingridentsIn
from food.schemas.junction_schema import testOut
from datetime import date
from ninja.orm import create_schema
from typing import List

class SpeciesOut(Schema):
     id: int
     name: str

class IngridentIn(Schema):
     name: str
     ingrident_type: int 
     calories: int


class ingridentOut (Schema):
     id: int
     name: str
     ingrident_type: SpeciesOut 
     calories: int

class RecipeSchema(Schema):
    name: str
    photo: str
    duration: int
    time_of_create: date
    recipe_description: str

class RecipeOut(RecipeSchema):
     id: int
     recipe_ingrident: List[ingridentOut]
     #amount: testOut

class RecipeIn(RecipeSchema):
     recipe_ingrident: List[int]
     

AutoRecipesOut = create_schema(Recipe, depth=1)
AutoRecipesIn = create_schema(Recipe , exclude=["id", "recipe_ingrident"] , depth= 1 )