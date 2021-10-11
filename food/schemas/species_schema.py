from food.models import Species
from ninja import Schema
from ninja.orm import create_schema


class speciesOut(Schema):
    id: int
    name: str

AutoSpeciesOut = create_schema(Species)
AutoSpeciesIn = create_schema(Species, exclude=["id"])