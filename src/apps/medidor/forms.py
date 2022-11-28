from django import forms
from .models import Medidor
from apps.equipo.models import Equipo


class RegisterMedidorForm(forms.ModelForm):
    nro_cliente = forms.CharField(required=True, max_length=255, label="Nro Cliente")
    nro_suministro = forms.CharField(required=True, max_length=255, label="Nro Suministro")
    equipo = forms.ModelChoiceField(queryset=Equipo.objects.all(),
                                    label="Equipos",
                                    widget=forms.Select(attrs={
                                        'class': 'form-control', 'style': "width: 100%"
                                    }), required=True)

    class Meta:
        model = Medidor
        fields = ["nro_cliente", "nro_suministro", "equipo"]
    