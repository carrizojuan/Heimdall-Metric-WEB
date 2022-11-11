from django import forms
from .models import Equipo

class RegisterEquipoForm(forms.ModelForm):
    nro_serie = forms.CharField(max_length=255, required=True, label="Numero de serie"
                                ,widget=forms.TextInput(attrs={'class': 'form-control'}))
    nombre = forms.CharField(required=False, label="Nombre",
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    activo = forms.BooleanField(required=False, label="¿Activo?",
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    latitud = forms.DecimalField(max_digits=8, decimal_places=6, label="Latitud", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    longitud = forms.DecimalField(max_digits=9, decimal_places=6, label="Longitud",  required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    app_eui = forms.CharField( required=False, max_length=255, label="App EUI")
    app_key = forms.CharField( required=False, max_length=255, label="App Key")
    dev_eui = forms.CharField( required=False, max_length=255, label="Dev EUI")
    
    class Meta:
        model = Equipo
        fields = ["nro_serie", "nombre", "activo","latitud", "longitud","app_eui","app_key", "dev_eui"]

"""
nro_serie = models.CharField(max_length=255, primary_key=True, verbose_name=_("equipo"), help_text=_("Nro. de serie del equipo"))
label = models.CharField(max_length=255, null=True, verbose_name=_("etiqueta"), help_text=_("Nombre de la etiqueta"))
name = models.CharField(max_length=255, null=False, verbose_name=_("nombre"), help_text=_("Nombre del equipo asignado"))
latitud = models.DecimalField(max_digits=8, decimal_places=6, null=True, verbose_name=_("latitud"), help_text=_("latitud"))
longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, verbose_name=_("longitud"), help_text=_("longitud"))
fecha_asignacion = models.DateTimeField(auto_now_add=True,  verbose_name=_("fecha de asignación"), help_text=_(
    "fecha de asignación del equipo"))
activo = models.BooleanField(default=False, verbose_name=_("activo"), help_text=_("equipo activo?"))
app_eui = models.CharField(null=True, max_length=255, default="", verbose_name=_("APPEUI"), help_text=_("APPEUI de credencial"))
app_key = models.CharField(null=True, max_length=255, default="", verbose_name=_("APPKEY"), help_text=_("APPKEY de credencial"))
dev_eui = models.CharField(null=True, max_length=255, default="", verbose_name=_("DEVEUI"), help_text=_("DEVEUI de credencial"))
"""