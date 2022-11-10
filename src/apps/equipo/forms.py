from django import forms
from .models import Equipo

class RegisterEquipoForm(forms.ModelForm):
    nombre = forms.CharField(required=False, label="Nombre",
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(required=False, label="¿Activo?",
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Equipo
        fields = ["nombre", "is_active"]
