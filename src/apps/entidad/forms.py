# from cProfile import label
# from pydoc import plain
# from pyexpat import model
from django import forms
# from django.contrib.admin.widgets import FilteredSelectMultiple
# from django.contrib.auth.models import Permission, Group
# from django.core.exceptions import ValidationError

from .models import Entidad, Miembro


class RegisterEntidadForm(forms.ModelForm):
    nombre = forms.CharField(required=False, label="Nombre",
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(required=False, label="¿Activo?",
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Entidad
        fields = ["nombre", "is_active"]


class RegisterMiembroForm(forms.ModelForm):
    nombre = forms.CharField(required=False, label="Nombre",
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    activo = forms.BooleanField(required=False, label="¿Activo?",
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Entidad
        fields = ["nombre", "activo"]