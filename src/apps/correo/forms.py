from django import forms
from apps.entidad.models import Entidad
from .models import EmailService

class EmailServiceForm(forms.ModelForm):
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
    class Meta:
        model = EmailService
        fields = ["host", "port", "user", "password", "use_tls", "entidad"]


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)