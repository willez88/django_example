from django.urls import path
from .views import PersonListView, PersonCreateView, PersonUpdateView, PersonDeleteView
from django.contrib.auth.decorators import login_required

app_name = 'person'

urlpatterns = [
    path('', login_required(PersonListView.as_view()), name='list'),
    path('registrar/', login_required(PersonCreateView.as_view()), name='create'),
    path('actualizar/<int:pk>/', login_required(PersonUpdateView.as_view()), name='update'),
    path('eliminar/<int:pk>/', login_required(PersonDeleteView.as_view()), name='delete'),
]
