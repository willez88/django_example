from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Person
from base.models import State, Municipality, Parish

class PersonForm(forms.ModelForm):
    """!
    Clase que contiene los campos del formulario

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-07-2018
    """

    ## Nombre
    first_name = forms.CharField(
        label=_('Nombres:'),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm', 'data-toggle': 'tooltip',
                'title': _('Indique los Nombres de la Persona'),
            }
        )
    )

    ## Apellido
    last_name = forms.CharField(
        label=_('Apellidos:'),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm', 'data-toggle': 'tooltip',
                'title': _('Indique los Apellidos de la Persona'),
            }
        )
    )

    ## Cédula de identidad
    identification_card = forms.CharField(
        label=_('Cédula:'),
        max_length=9,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm', 'data-toggle': 'tooltip',
                'title': _('Indique la Cédula de la Persona'),
            }
        )
    )

    ## Número telefónico
    phone = forms.CharField(
        label=_('Teléfono:'),
        max_length=15,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm', 'placeholder': '+58-000-0000000',
                'data-toggle': 'tooltip', 'data-mask': '+00-000-0000000',
                'title': _('Indique el número telefónico de contacto'),
            }
        ),
        help_text=_('(país)-área-número')
    )

    ## Correo Electrónico
    email = forms.EmailField(
        label=_('Correo Electrónico:'),
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control form-control-sm email-mask', 'placeholder': _("Correo de contacto"),
                'data-toggle': 'tooltip',
                'title': _('Indique el correo electrónico de contacto con el usuario')
            }
        )
    )

    ## Estado
    state = forms.ModelChoiceField(
        label=_('Estado:'), queryset=State.objects.all(), empty_label=_('Seleccione...'),
        widget=forms.Select(attrs={
            'class': 'form-control form-control-sm select2', 'data-toggle': 'tooltip',
            'title': _('Seleccione el estado en donde se encuentra ubicada'),
            'onchange': "combo_update(this.value,'base','Municipality','state','pk','name','id_municipality')",
        })
    )

    ## Municipio
    municipality = forms.ModelChoiceField(
        label=_('Municipio:'), queryset=Municipality.objects.all(), empty_label=_('Seleccione...'),
        widget=forms.Select(attrs={
            'class': 'form-control form-control-sm select2', 'data-toggle': 'tooltip', 'disabled': 'true',
            'title': _('Seleccione el municipio en donde se encuentra ubicada'),
            'onchange': "combo_update(this.value,'base','Parish','municipality','pk','name','id_parish')",
        })
    )

    ## Parroquia
    parish = forms.ModelChoiceField(
        label=_('Parroquia:'), queryset=Parish.objects.all(), empty_label=_('Seleccione...'),
        widget=forms.Select(attrs={
            'class': 'form-control form-control-sm select2', 'data-toggle': 'tooltip', 'disabled': 'true',
            'title': _('Seleccione la parroquia en donde se encuentra ubicada'),
        })
    )

    ## Dirección
    address = forms.CharField(
        label=_('Dirección:'),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm', 'data-toggle': 'tooltip',
                'title': _('Indique la dirección exacta'),
            }
        )
    )

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez (paez.william8 at gmail.com)
        @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 06-07-2018
        """

        ## Modelo
        model = Person

        ## Campos a expluir
        exclude = ['user']
