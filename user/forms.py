from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class ProfileForm(forms.ModelForm):
    """!
    Clase que contiene los campos del formulario de perfil del usuario

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Username para identificar al usuario
    username = forms.CharField(
        label=_('Nombre de Usuario:'), max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique el nombre de usuario'),
            }
        )
    )

    # Nombres del usuario
    first_name = forms.CharField(
        label=_('Nombres:'), max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique los Nombres'),
            }
        )
    )

    # Apellidos del usuario
    last_name = forms.CharField(
        label=_('Apellidos:'), max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique los Apellidos'),
            }
        )
    )

    # Correo del usuario
    email = forms.EmailField(
        label=_('Correo Electrónico:'), max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control input-sm email-mask',
                'data-toggle': 'tooltip',
                'title': _('Indique el correo electrónico')
            }
        )
    )

    # Teléfono del usuario
    phone = forms.CharField(
        label=_('Teléfono:'), max_length=15,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'placeholder': '+58-000-0000000',
                'data-mask': '+00-000-0000000',
                'title': _('Indique el número telefónico')
            }
        )
    )

    # Contraseña de acceso del usuario
    password = forms.CharField(
        label=_('Contraseña:'), max_length=128,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique una contraseña de aceso al sistema')
            }
        )
    )

    # Confirmación de contraseña de acceso del usuario
    confirm_password = forms.CharField(
        label=_('Confirmar Contraseña:'), max_length=128,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique nuevamente la contraseña de aceso al\
                sistema')
            }
        )
    )

    def clean_email(self):
        """!
        Función que permite validar si el correo del usuario ya esta registrado
            en el sistema

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Mensaje de error en caso de que el correo ya esté registrado
            en el sistema
        """

        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError(_('El correo ya esta registrado'))
        return email

    def clean_confirm_password(self):
        """!
        Función que permite validar si ambas contraseñas son iguales

        @author William Páez (paez.william8 at gmail.com)
        @date 03-08-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Mensaje de error en caso de que las contraseñas sean distintas
        """

        confirm_password = self.cleaned_data['confirm_password']
        password = self.cleaned_data.get('password')
        if password != confirm_password:
            raise forms.ValidationError(_('La contraseña no es la misma'))

        return confirm_password

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez (paez.william8 at gmail)
        """

        model = User
        exclude = ['profile', 'date_joined']


class ProfileUpdateForm(ProfileForm):
    """!
    Clase que contiene los campos del formulario de perfil del usuario para
        actualizar los datos

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    def __init__(self, *args, **kwargs):
        """!
        Función que inicializa la clase del formulario para actualizar los
            datos

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @param *args <b>{tupla}</b> Tupla de valores, inicialmente vacia
        @param *kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        """

        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['password'].required = False
        self.fields['confirm_password'].required = False
        self.fields['password'].widget.attrs['disabled'] = True
        self.fields['confirm_password'].widget.attrs['disabled'] = True

    def clean_email(self):
        """!
        función que permite validar el campo de correo electronico

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Mensaje de error en caso de que el correo electronico ya se
            encuentre registrado
        """

        email = self.cleaned_data['email']
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(_('El correo ya esta registrado'))
        return email

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez (paez.william8 at gmail.com)
        @date 03-08-2018
        """

        model = User
        exclude = [
            'profile', 'password', 'confirm_password', 'date_joined',
            'last_login', 'is_active', 'is_superuser', 'is_staff'
        ]
