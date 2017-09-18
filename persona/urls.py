from django.conf.urls import url
from .views import PersonaList, PersonaCreate, PersonaUpdate, PersonaDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(PersonaList.as_view()), name='persona_lista'),
    url(r'^registro/$', login_required(PersonaCreate.as_view()), name='persona_registro'),
    url(r'^actualizar/(?P<pk>\d+)/$', login_required(PersonaUpdate.as_view()), name='persona_actualizar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(PersonaDelete.as_view()), name='persona_eliminar'),
]
