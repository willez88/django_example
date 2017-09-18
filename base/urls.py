from django.conf.urls import url
from .views import inicio

urlpatterns = [
    url(r'^$', inicio, name='inicio'),
]
