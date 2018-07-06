from django.urls import path, re_path
from .views import HomeView, Error403View
from .ajax import ComboUpdateView

app_name = 'base'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('error-403/', Error403View.as_view(), name = "error_403"),
]

## URLs de peticiones AJAX
urlpatterns += [
    re_path(r'^ajax/actualizar-combo/?$', ComboUpdateView.as_view(), name='combo_update'),
]
