from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Person
from .forms import PersonForm
from base.models import Parish
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from base.constant import CREATE_MESSAGE, UPDATE_MESSAGE, DELETE_MESSAGE

class PersonListView(ListView):
    model = Person
    template_name = 'person/list.html'

    def get_queryset(self):
        queryset = Person.objects.filter(user=self.request.user)
        return queryset

class PersonCreateView(SuccessMessageMixin, CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'person/create.html'
    success_url = reverse_lazy('person:list')
    success_message = CREATE_MESSAGE

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.parish = form.cleaned_data['parish']
        self.object.save()
        return super(PersonCreateView, self).form_valid(form)

class PersonUpdateView(SuccessMessageMixin, UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'person/create.html'
    success_url = reverse_lazy('person:list')
    success_message = UPDATE_MESSAGE

    def dispatch(self, request, *args, **kwargs):
        if Person.objects.filter(pk=self.kwargs['pk'],user=self.request.user):
            return super(PersonUpdateView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')

    def get_initial(self):
        initial_data = super(PersonUpdateView, self).get_initial()
        initial_data['state'] = self.object.parish.municipality.state
        initial_data['municipality'] = self.object.parish.municipality
        return initial_data

class PersonDeleteView(SuccessMessageMixin, DeleteView):
    model = Person
    template_name = 'person/delete.html'
    success_url = reverse_lazy('person:list')
    success_message = DELETE_MESSAGE

    def dispatch(self, request, *args, **kwargs):
        if Person.objects.filter(pk=self.kwargs['pk'],user=self.request.user):
            return super(PersonDeleteView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PersonDeleteView, self).delete(request, *args, **kwargs)
