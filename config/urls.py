from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from ninja import NinjaAPI
from food.controllers.species import species_controller
from food.controllers.ingridentsControl import ingridents_controller
from food.controllers.recipes_controller import recipes_controller
from rest_auth.controllers.Auth_controller import auth_controller
api = NinjaAPI(
    version='1.0.0',
    title='client API v1',
    description='API documentation',
)
api.add_router('/species', species_controller)
api.add_router('/ingridents', ingridents_controller )
api.add_router('/recipes', recipes_controller)
api.add_router('/auth', auth_controller)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]

# if settings.DEBUG:
#     urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
