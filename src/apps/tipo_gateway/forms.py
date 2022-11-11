from django import forms
from .models import TipoGateway, Consola


class RegisterTipoGatewayForm(forms.ModelForm):
    nombre = forms.CharField(required=True, label="Nombre",
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = TipoGateway
        fields = ["nombre"]


# class RegisterConsolaForm(forms.ModelForm):
#     nombre = forms.CharField(required=False, label="Nombre",
#                               widget=forms.TextInput(attrs={'class': 'form-control'}))
#     base_url = forms.CharField(required=True, label="Base URL",
#                               widget=forms.TextInput(attrs={'class': 'form-control'}))
#     apikey = forms.CharField(required=True, label="APIKEY",
#                               widget=forms.TextInput(attrs={'class': 'form-control'}))
#     class Meta:
#         model = Consola
#         fields = ["nombre", "base_url", "apikey", "nombre_tipo_gateway"]


class DetalleConsolaForm(forms.ModelForm):
    nombre = forms.CharField(required=False, label="Nombre",
                              widget=forms.TextInput(attrs={'class': 'form-control'}),disabled=True)
    base_url = forms.CharField(required=True, label="Base URL",
                              widget=forms.TextInput(attrs={'class': 'form-control'}),disabled=True)
    apikey = forms.CharField(required=True, label="APIKEY",
                              widget=forms.TextInput(attrs={'class': 'form-control'}),disabled=True)
    # nombre_tipo_gateway = forms.CharField(required=True, label="Tipo Gateway",
    #                           widget=forms.TextInput(attrs={'class': 'form-control'}),disabled=True)

    class Meta:
        model = Consola
        fields = ["nombre", "base_url", "apikey"]
