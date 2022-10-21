from pydoc import plain
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Permission, Group
from django.core.exceptions import ValidationError


from .models import Usuario


""" class UsuarioForm(forms.ModelForm):
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nombres = forms.CharField(required=False, label="Nombres",
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellidos = forms.CharField(required=False, label="Apellidos",
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    nombreUsuario = forms.CharField(required=False, label="Nombre de Usuario",
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    es_admin = forms.BooleanField(required=False, label="¿Es Administrador?",
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    is_staff = forms.BooleanField(required=False, label="¿Es Staff?",
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    is_active = forms.BooleanField(required=False, label="¿Está Activo?",
                                   widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    user_permissions = forms.ModelMultipleChoiceField(label="Permisos del usuario", required=False,
                                                      queryset=Permission.objects.all(),
                                                      widget=FilteredSelectMultiple("Permisos", is_stacked=False))

    groups = forms.ModelMultipleChoiceField(label="Grupos del usuario", required=False, queryset=Group.objects.all(),
                                            widget=FilteredSelectMultiple("Grupo", is_stacked=False))

    class Meta:
        model = Usuario
        fields = ['nombres', 'apellidos', 'nombre_usuario', 'email', 'entidad', 'es_admin', 'is_staff', 'is_active',
                  'user_permissions', 'groups']

    class Media:
        css = {
            'all': ('/static/admin/css/widgets.css', '/static/admin/css/responsive.css'),
        }
        js = ('/admin/jsi18n',)

    def __init__(self, disabled_fields=[], *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)

        if disabled_fields:
            for field in disabled_fields:
                self.fields[field].widget.attrs['readonly'] = True

    def clean_groups(self):
        groups = self.cleaned_data['groups']

        if len(groups) > 1:
            raise ValidationError('Seleccione solo un grupo.')
        return groups

    def clean(self):
        cleaned_data = super(UsuarioForm, self).clean()

        user_permissions = self.cleaned_data.get('user_permissions', None)
        groups = self.cleaned_data.get('groups', None)

        if user_permissions and groups:
            self.add_error('user_permissions',
                           'Un usuario solo puede pertenecer a un grupo, o bien solo tener permisos particulares, verifique.')

        return self.cleaned_data


class GroupForm(forms.ModelForm):
    name = forms.CharField(label="Nombre del Grupo", widget=forms.TextInput(attrs={'class': 'form-control'}))
    permissions = forms.ModelMultipleChoiceField(label="Permisos", required=False, queryset=Permission.objects.all(),
                                                 widget=FilteredSelectMultiple("Grupo", is_stacked=False))

    class Meta:
        model = Group
        fields = ['name', 'permissions']

    class Media:
        css = {
            'all': ('/static/admin/css/widgets.css', '/static/admin/css/responsive.css'),
        }
        js = ('/admin/jsi18n',)


class PassForm(forms.ModelForm):
    password = forms.EmailField(required=True,
                                widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': "Contraseña"}))
    confirm_password = forms.CharField(required=True,
                                       widget=forms.PasswordInput(
                                           attrs={'class': 'input100 pwds', 'placeholder': "Confirmar Contraseña"}))

    class Meta:
        model = Usuario
        fields = ['password', 'confirm_password'] """


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-label form-control'}
    ))
    nombre_usuario = forms.CharField(required=True,label="Nombre de Usuario",
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    nombres = forms.CharField(required=False, label="Nombres",
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellidos = forms.CharField(required=False, label="Apellidos",
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.EmailField(required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))

    class Meta:
        model = Usuario
        fields = ["nombre_usuario", "email", "nombres", "apellidos","password"]


