from django.conf.urls import url
from .views import InicioView, Error403View

urlpatterns = [
    url(r'^$', InicioView.as_view(), name='inicio'),
    url(r'^error-403/$', Error403View.as_view(), name = "error_403"),
]
