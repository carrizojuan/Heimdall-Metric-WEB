from django import forms
from .models import Equipo

class RegisterEquipoForm(forms.ModelForm):
    nro_serie = forms.CharField(max_length=255, required=True, label="Numero de serie"
                                ,widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(required=False, label="Nombre",
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    label = forms.CharField(max_length=255, required=False, label = "Etiqueta", widget=forms.TextInput(attrs={'class': 'form-control'}))
    activo = forms.BooleanField(required=False, label="¿Activo?",
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    latitud = forms.DecimalField(max_digits=8, decimal_places=6, label="Latitud", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    longitud = forms.DecimalField(max_digits=9, decimal_places=6, label="Longitud",  required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    app_eui = forms.CharField( required=False, max_length=255, label="App EUI")
    app_key = forms.CharField( required=False, max_length=255, label="App Key")
    dev_eui = forms.CharField( required=False, max_length=255, label="Dev EUI")
    
    class Meta:
        model = Equipo
        fields = ["nro_serie", "name", "label", "activo","latitud", "longitud","app_eui","app_key", "dev_eui"]


class EditEquipoForm(forms.ModelForm):
    name = forms.CharField(required=False, label="Nombre",
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    label = forms.CharField(max_length=255, required=False, label = "Etiqueta", widget=forms.TextInput(attrs={'class': 'form-control'}))
    activo = forms.BooleanField(required=False, label="¿Activo?",
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    latitud = forms.DecimalField(max_digits=8, decimal_places=6, label="Latitud", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    longitud = forms.DecimalField(max_digits=9, decimal_places=6, label="Longitud",  required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Equipo
        fields = ["name", "label", "activo","latitud", "longitud"]