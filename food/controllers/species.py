from django.http import response
from food.schemas.species_schema import AutoSpeciesOut , AutoSpeciesIn
from ninja import Router
from food.models import Species
from typing import List
from ninja import Query


species_controller = Router(tags=["species"])

@species_controller.get("/retrieve", response= List[AutoSpeciesOut])
def species_get_all(request):
    return Species.objects.all()

@species_controller.post("/create" , response = AutoSpeciesOut )
def species_create(request , payload: AutoSpeciesIn):
    species = Species.objects.create(**payload.dict())
    return species

@species_controller.get('/retrieve/{species_id}', response= AutoSpeciesOut)
def species_get(request, species_id: int):
    species = Species.objects.get(id = species_id)
    return species

@species_controller.put('/update/{species_id}', response= AutoSpeciesOut)
def species_put(request, payload: AutoSpeciesIn, species_id: int):
    species = Species.objects.get(id = species_id)
    for key , value in payload.dict().items():
        setattr(species,key,value)
    species.save()
    return {"success": True}