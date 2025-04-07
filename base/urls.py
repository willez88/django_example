from django.urls import include, path, re_path

from .ajax import ComboUpdateView
from .views import Error403View, HomeView

app_name = 'base'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('error-403/', Error403View.as_view(), name='error_403'),
]

# URLs de peticiones AJAX
urlpatterns += [
    re_path(
        r'^ajax/combo-update/?$',
        ComboUpdateView.as_view(),
        name='combo_update'
    ),
]
