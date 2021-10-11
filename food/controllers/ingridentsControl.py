from food.models import Ingrident
from food.schemas.ingridents_schema import ingridentAutoIn , ingridentAutoOut , ingridentOut , ingridentsIn
from typing import List
from ninja import Router

ingridents_controller = Router(tags=["ingridents"])

@ingridents_controller.get("/retreiveall", response=List[ingridentOut] )
def ingridents_all(request):
    ingrident = Ingrident.objects.all()
    return ingrident

@ingridents_controller.get("/retreive/{ingrident_id}" , response= ingridentAutoOut)
def ingridents_get(request, ingrident_id: int  ):
    ingrident = Ingrident.objects.get(id = ingrident_id)
    return ingrident

@ingridents_controller.post("/create" , response=ingridentAutoOut)
def ingridents_post(request , payload: ingridentAutoIn):
    pob = payload.ingrident_type
    del payload.ingrident_type
    ingrident = Ingrident.objects.create(**payload.dict(), ingrident_type_id = pob )
    return ingrident