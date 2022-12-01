from django import forms
from .models import Medidor
from apps.equipo.models import Equipo


class RegisterMedidorForm(forms.ModelForm):
    nro_cliente = forms.UUIDField(required=True, label="Nro Cliente",disabled=True)
    nro_suministro = forms.IntegerField(required=True, label="Nro Suministro")
    equipo = forms.ModelChoiceField(queryset=Equipo.objects.all(),
                                    label="Equipos",
                                    widget=forms.Select(attrs={
                                        'class': 'form-control', 'style': "width: 100%"
                                    }), required=True)

    class Meta:
        model = Medidor
        fields = ["nro_cliente", "nro_suministro", "equipo"]


class AsociarMedidorForm(forms.ModelForm):
    nro_cliente = forms.UUIDField(required=True, label="Nro Cliente",disabled=True)
    nro_suministro = forms.IntegerField(required=True, label="Nro Suministro")
    equipo = forms.ModelChoiceField(queryset=Equipo.objects.all(),
                                    label="Equipos",
                                    widget=forms.Select(attrs={
                                        'class': 'form-control', 'style': "width: 100%"
                                    }), required=True)

    class Meta:
        model = Medidor
        fields = ["nro_cliente","equipo", "nro_suministro"]

    def __init__(self, *args,**kwargs):
        initial = kwargs.get("initial",{})
        self.nro_cliente = initial.get("nro_cliente")
        super(AsociarMedidorForm, self).__init__(*args,**kwargs)