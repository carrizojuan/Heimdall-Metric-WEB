
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.utils.mixins import AdminRequiredMixin
from .forms import EmailServiceForm
from .models import EmailService
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect

class CreateEmailServiceView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = EmailService
    template_name = 'correo/crear_servicio.html'
    form_class = EmailServiceForm

    def get_success_url(self, **kwargs):
        return reverse('dashboard_admin', args=[])

    def form_valid(self, form):
        f = form.save(commit=True)
        return super(CreateEmailServiceView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(CreateEmailServiceView, self).get_context_data(**kwargs)
        return context


class EmailServiceDetailView(DetailView):
    model = EmailService
    template_name = 'correo/email_service_detail.html'
    context_object_name = "email_service"


class EmailServiceListView(ListView):
    model = EmailService
    template_name = 'correo/email_service_list.html'


def email_service_delete(request, pk):

    # Obtener el servicio de correo electrónico a eliminar
    service = get_object_or_404(EmailService, pk=pk)
    print(service)
    # Eliminar el servicio de correo electrónico
    service.delete()
    
    # Redirigir al usuario a la lista de servicios de correo electrónico
    return HttpResponseRedirect(reverse("email_service:email_service_list"))


class EmailServiceUpdateView(UpdateView):
    model = EmailService
    form_class = EmailServiceForm
    template_name = 'correo/email_service_update.html'

    def get_success_url(self):
        return reverse('email_service:email_service_detail', kwargs={'pk': self.kwargs['pk']})