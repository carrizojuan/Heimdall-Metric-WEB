# from cProfile import label
# from pydoc import plain
# from pyexpat import model
from django import forms
# from django.contrib.admin.widgets import FilteredSelectMultiple
# from django.contrib.auth.models import Permission, Group
# from django.core.exceptions import ValidationError

from .models import Entidad, Miembro
from apps.usuario.models import Usuario


class RegisterEntidadForm(forms.ModelForm):
    nombre = forms.CharField(required=False, label="Nombre",
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(required=False, label="¿Activo?",
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Entidad
        fields = ["nombre", "is_active"]

ROL_SELECCION = (
    (1, 'ADMINISTRADOR'),
    (2, 'MONITOR'),
)


class RegisterMiembroForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(),
                                    label="Usuarios",
                                    widget=forms.Select(attrs={
                                        'class': 'form-control', 'style': "width: 100%"
                                    }), required=True)
    rol = forms.ChoiceField(choices=ROL_SELECCION,
                                         label="Rol",
                                         widget=forms.RadioSelect(attrs={
                                             'class': '',
                                         }), required=True)

    activo = forms.BooleanField(required=True, label="¿Activo?",
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    def __init__(self, *args, **kwargs):
        # print("->>>>",kwargs)
        # qs = kwargs.pop('usuarios')
        super(RegisterMiembroForm, self).__init__(*args, **kwargs)
        # print("->>>>", kwargs, args)
        # self.fields['usuario'].queryset = qs

    class Meta:
        model = Miembro
        fields = ["usuario", "rol", "activo"]

