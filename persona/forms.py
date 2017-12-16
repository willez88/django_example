from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Persona

class PersonaForm(forms.ModelForm):
    nombre = forms.CharField(
        label=_("Nombres:"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style': 'width:250px',
                'title': _("Indique los Nombres de la Persona"),
            }
        )
    )

    apellido = forms.CharField(
        label=_("Apellidos:"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style': 'width:250px',
                'title': _("Indique los Apellidos de la Persona"),
            }
        )
    )

    cedula = forms.CharField(
        label=_("Cédula:"),
        max_length=9,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style': 'width:250px',
                'title': _("Indique la Cédula de la Persona"),
            }
        )
    )

    ## Número telefónico de contacto con el usuario
    telefono = forms.CharField(
        label=_("Teléfono:"),
        max_length=18,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'placeholder': '+58-000-0000000',
                'data-rule-required': 'true', 'data-toggle': 'tooltip', 'style': 'width:250px',
                'title': _("Indique el número telefónico de contacto"), 'data-mask': '+00-000-0000000'
            }
        ),
        help_text=_("(país)-área-número")
    )

    correo = forms.EmailField(
        label=_("Correo Electrónico:"),
        max_length=100,
        help_text=_("Cédula de Identidad del usuario"),
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control input-sm email-mask', 'placeholder': _("Correo de contacto"),
                'data-toggle': 'tooltip', 'data-rule-required': 'true', 'style': 'width:250px',
                'title': _("Indique el correo electrónico de contacto con el usuario.")
            }
        )
    )

    class Meta:
        model = Persona
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
