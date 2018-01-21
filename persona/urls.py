from django.urls import path
from .views import PersonaList, PersonaCreate, PersonaUpdate, PersonaDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(PersonaList.as_view()), name='persona_lista'),
    path('registro/', login_required(PersonaCreate.as_view()), name='persona_registro'),
    path('actualizar/<int:pk>/', login_required(PersonaUpdate.as_view()), name='persona_actualizar'),
    path('eliminar/<int:pk>/', login_required(PersonaDelete.as_view()), name='persona_eliminar'),
]
