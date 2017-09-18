from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^cambiar-clave/$', login_required(auth_views.PasswordChangeView.as_view(template_name='password_change_form.html')), name='password_change'),
    url(r'^cambiar-clave-hecho/$', login_required(auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html')), name='password_change_done'),
]
