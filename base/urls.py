from django.urls import path
from .views import InicioView, Error403View

app_name = 'base'

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('error-403/', Error403View.as_view(), name = "error_403"),
]
