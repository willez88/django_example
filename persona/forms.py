from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Persona

class PersonaForm(forms.ModelForm):
    nombre = forms.CharField(
        label=_("Nombres:"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'title': _("Indique los Nombres de la Persona"),
            }
        )
    )

    apellido = forms.CharField(
        label=_("Apellidos:"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'title': _("Indique los Apellidos de la Persona"),
            }
        )
    )

    cedula = forms.CharField(
        label=_("Cédula:"),
        max_length=9,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'title': _("Indique la Cédula de la Persona"),
            }
        )
    )

    ## Número telefónico de contacto con el usuario
    telefono = forms.CharField(
        label=_("Teléfono:"),
        max_length=18,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'placeholder': '(+058)-000-0000000',
                'data-rule-required': 'true', 'data-toggle': 'tooltip',
                'title': _("Indique el número telefónico de contacto"), 'data-mask': '(+000)-000-0000000'
            }
        ),
        help_text=_("(país)-área-número")
    )

    correo = forms.EmailField(
        label=_("Correo Electrónico:"),
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control input-sm email-mask', 'placeholder': _("Correo de contacto"),
                'data-toggle': 'tooltip', 'size': '30', 'data-rule-required': 'true',
                'title': _("Indique el correo electrónico de contacto con el usuario. "
                           "No se permiten correos de hotmail")
            }
        )
    )

    class Meta:
        model = Persona
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
