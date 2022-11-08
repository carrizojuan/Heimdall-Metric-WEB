from django import forms
from .models import TipoGateway


class RegisterTipoGatewayForm(forms.ModelForm):
    nombre = forms.CharField(required=True, label="Nombre",
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = TipoGateway
        fields = ["nombre"]
