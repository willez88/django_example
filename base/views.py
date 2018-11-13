from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .serializers import CountrySerializer
from .models import Country, State
from rest_framework import generics

# Create your views here.

class HomeView(TemplateView):
    """!
    Clase que muestra la página inicial

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 06-07-2018
    """

    template_name = 'base/base.html'

class Error403View(TemplateView):
    """!
    Clase que muestra la página de error de permisos

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 06-07-2018
    """

    template_name = 'base/error.403.html'

class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    #http_method_names = ['get']
