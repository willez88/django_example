from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Persona
from .forms import PersonaForm

# Create your views here.

class PersonaList(ListView):
    model = Persona
    template_name = "persona.lista.html"

    def get_queryset(self):
        queryset = Persona.objects.filter(user=self.request.user)
        return queryset

class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = "persona.registro.html"
    success_url = reverse_lazy('persona_lista')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(PersonaCreate, self).form_valid(form)

class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = "persona.registro.html"
    success_url = reverse_lazy('persona_lista')

    def dispatch(self, request, *args, **kwargs):
        user = User.objects.get(username=self.request.user.username)
        if not Persona.objects.filter(pk=self.kwargs['pk'],user=user):
            return redirect('error_403')
        return super(PersonaUpdate, self).dispatch(request, *args, **kwargs)

class PersonaDelete(DeleteView):
    model = Persona
    template_name = "persona.eliminar.html"
    success_url = reverse_lazy('persona_lista')

    def dispatch(self, request, *args, **kwargs):
        user = User.objects.get(username=self.request.user.username)
        if not Persona.objects.filter(pk=self.kwargs['pk'],user=user):
            return redirect('error_403')
        return super(PersonaDelete, self).dispatch(request, *args, **kwargs)
