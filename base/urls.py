from django.urls import path, re_path, include
from .views import HomeView, Error403View
from .ajax import ComboUpdateView
from rest_framework import routers
from .views import CountryViewSet

app_name = 'base'

router = routers.DefaultRouter()
router.register(r'countries', CountryViewSet)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('error-403/', Error403View.as_view(), name = 'error_403'),

    path('api/', include(router.urls)),
]

## URLs de peticiones AJAX
urlpatterns += [
    re_path(r'^ajax/combo-update/?$', ComboUpdateView.as_view(), name='combo_update'),
]
