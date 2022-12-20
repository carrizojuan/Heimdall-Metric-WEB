from django import forms
from apps.entidad.models import Entidad

class EmailServiceForm(forms.Form):
    host = forms.CharField(max_length=100)
    port = forms.IntegerField()
    user = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, required=False)
    use_tls = forms.BooleanField()
    entidad = forms.ModelChoiceField(queryset=Entidad.objects.all(),
                                    label="Entidades",
                                    widget=forms.Select(attrs={
                                        'class': 'form-control', 'style': "width: 100%"
                                    }), required=True)