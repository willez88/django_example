from django.urls import path
from .views import PersonListView, PersonCreateView, PersonUpdateView, PersonDeleteView
from django.contrib.auth.decorators import login_required

app_name = 'person'

urlpatterns = [
    path('list/', login_required(PersonListView.as_view()), name='list'),
    path('create/', login_required(PersonCreateView.as_view()), name='create'),
    path('update/<int:pk>/', login_required(PersonUpdateView.as_view()), name='update'),
    path('delete/<int:pk>/', login_required(PersonDeleteView.as_view()), name='delete'),
]
