from django.urls import path
from .views import PersonaList, PersonaCreate, PersonaUpdate, PersonaDelete
from django.contrib.auth.decorators import login_required

app_name = 'persona'

urlpatterns = [
    path('', login_required(PersonaList.as_view()), name='listar'),
    path('registro/', login_required(PersonaCreate.as_view()), name='registrar'),
    path('actualizar/<int:pk>/', login_required(PersonaUpdate.as_view()), name='actualizar'),
    path('eliminar/<int:pk>/', login_required(PersonaDelete.as_view()), name='eliminar'),
]
