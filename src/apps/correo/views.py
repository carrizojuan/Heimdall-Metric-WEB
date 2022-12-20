from django.shortcuts import render, redirect
from django.views import View
from .forms import EmailServiceForm
from .models import EmailService, Entidad

class CreateEmailServiceView(View):
    def get(self, request):
        form = EmailServiceForm()
        return render(request, 'correo/crear_servicio.html', {'form': form})

    def post(self, request):
        form = EmailServiceForm(request.POST)
        if form.is_valid():
            entidad = Entidad.objects.get(id=form.cleaned_data['id_entidad'])  # Obtén la entidad
            email_service = EmailService(
                host=form.cleaned_data['host'],
                port=form.cleaned_data['port'],
                user=form.cleaned_data['user'],
                password=form.cleaned_data['password'],
                use_tls=form.cleaned_data['use_tls'],
                id_entidad=entidad,
            )
            email_service.save()  # Guarda la instancia del modelo en la base de datos
            return redirect('email_service_success')
        return render(request, 'correo/crear_servicio.html', {'form': form})