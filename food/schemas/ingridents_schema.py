from food.models import Ingrident
from ninja import Schema
from ninja.orm import create_schema
from food.schemas.species_schema import AutoSpeciesOut

class testOut(Schema):
    id: int
    name: str


class ingridentsSchema(Schema):
    name: str
    calories: int

class ingridentOut(ingridentsSchema):
    id: int
    ingrident_type: AutoSpeciesOut
  

class ingridentsIn(ingridentsSchema):
    ingrident_type: int

ingridentAutoOut = create_schema(Ingrident)

ingridentAutoIn = create_schema(Ingrident, exclude=["id"])
    
