from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Person
from base.models import State, Municipality, Parish

class PersonForm(forms.ModelForm):

    first_name = forms.CharField(
        label=_("Nombres:"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm', 'data-toggle': 'tooltip',
                'title': _("Indique los Nombres de la Persona"),
            }
        )
    )

    last_name = forms.CharField(
        label=_("Apellidos:"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm', 'data-toggle': 'tooltip',
                'title': _("Indique los Apellidos de la Persona"),
            }
        )
    )

    identification_card = forms.CharField(
        label=_("Cédula:"),
        max_length=9,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm', 'data-toggle': 'tooltip',
                'title': _("Indique la Cédula de la Persona"),
            }
        )
    )

    ## Número telefónico de contacto con el usuario
    phone = forms.CharField(
        label=_("Teléfono:"),
        max_length=15,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm', 'placeholder': '+58-000-0000000',
                'data-toggle': 'tooltip', 'data-mask': '+00-000-0000000',
                'title': _("Indique el número telefónico de contacto"),
            }
        ),
        help_text=_("(país)-área-número")
    )

    email = forms.EmailField(
        label=_("Correo Electrónico:"),
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control form-control-sm email-mask', 'placeholder': _("Correo de contacto"),
                'data-toggle': 'tooltip',
                'title': _("Indique el correo electrónico de contacto con el usuario.")
            }
        )
    )

    ## Estado donde se ecnuetra ubicado el municipio
    state = forms.ModelChoiceField(
        label=_("Estado:"), queryset=State.objects.all(), empty_label=_("Seleccione..."),
        widget=forms.Select(attrs={
            'class': 'form-control form-control-sm select2', 'data-toggle': 'tooltip',
            'title': _("Seleccione el estado en donde se encuentra ubicada"),
            'onchange': "combo_update(this.value,'base','Municipality','state','pk','name','id_municipality')",
        })
    )

    ## Municipio donde se encuentra ubicada la parroquia
    municipality = forms.ModelChoiceField(
        label=_("Municipio:"), queryset=Municipality.objects.all(), empty_label=_("Seleccione..."),
        widget=forms.Select(attrs={
            'class': 'form-control form-control-sm select2', 'data-toggle': 'tooltip', 'disabled': 'true',
            'title': _("Seleccione el municipio en donde se encuentra ubicada"),
            'onchange': "combo_update(this.value,'base','Parish','municipality','pk','name','id_parish')",
        })
    )

    ## Parroquia donde se encuentra ubicado el consejo comunal
    parish = forms.ModelChoiceField(
        label=_("Parroquia:"), queryset=Parish.objects.all(), empty_label=_("Seleccione..."),
        widget=forms.Select(attrs={
            'class': 'form-control form-control-sm select2', 'data-toggle': 'tooltip', 'disabled': 'true',
            'title': _("Seleccione la parroquia en donde se encuentra ubicada"),
        })
    )

    address = forms.CharField(
        label=_("Dirección:"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm', 'data-toggle': 'tooltip',
                'title': _("Indique la dirección exacta"),
            }
        )
    )

    class Meta:
        model = Person
        exclude = ['user']
