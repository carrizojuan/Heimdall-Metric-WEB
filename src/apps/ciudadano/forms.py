from .models import AuthUsuario
from django import forms


class CiudadanoForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-label form-control'}
                                                                    ))
    nombre_usuario = forms.CharField(required=True, label="Nombre de Usuario",
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
    nombres = forms.CharField(required=False, label="Nombres",
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellidos = forms.CharField(required=False, label="Apellidos",
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    nro_cliente = forms.CharField(required=False, label="Nro. Cliente",
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}), disabled=True)

    class Meta:
        model = AuthUsuario
        fields = ["nombre_usuario", "email", "nombres", "apellidos", "nro_cliente"]


class DetalleCiudadanoForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-label form-control'}
                                                                    ),disabled=True)
    nombre_usuario = forms.CharField(required=True, label="Nombre de Usuario",
                                     widget=forms.TextInput(attrs={'class': 'form-control'}),disabled=True)
    nombres = forms.CharField(required=False, label="Nombres",
                              widget=forms.TextInput(attrs={'class': 'form-control'}),disabled=True)
    apellidos = forms.CharField(required=False, label="Apellidos",
                                widget=forms.TextInput(attrs={'class': 'form-control'}),disabled=True)
    nro_cliente = forms.CharField(required=False, label="Nro. Cliente",
                                widget=forms.NumberInput(attrs={'class': 'form-control'}),disabled=True)

    class Meta:
        model = AuthUsuario
        fields = ["nombre_usuario", "email", "nombres", "apellidos", "nro_cliente"]
