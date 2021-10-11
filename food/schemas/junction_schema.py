from food.models import Test
from ninja import Schema
from ninja.orm import create_schema

testOut = create_schema(Test , exclude=["id" , "recipe", "ingrident"])