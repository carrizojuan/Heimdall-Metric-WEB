from django.contrib.auth.mixins import LoginRequiredMixin
from apps.utils.mixins import AdminRequiredMixin
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from .models import Medidor
from .forms import RegisterMedidorForm

class CrearMedidorView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Medidor
    template_name = 'medidor/crear_medidor.html'
    form_class = RegisterMedidorForm

    def get_success_url(self, **kwargs):
        return reverse('medidor:mensaje_creado.html', args=[])

    def form_valid(self, form):
        f = form.save(commit=True)
        return super(CrearMedidorView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CrearMedidorView, self).get_context_data(**kwargs)
        context['sidebar_active'] = 'medidores'
        context['sidebar_active_sub'] = 'crear'
        return context
    

class ListMedidoresView(LoginRequiredMixin, AdminRequiredMixin, ListView):

    model = Medidor
    template_name = "medidor/lista_medidores.html"
    context_object_name = 'medidor'

    def get_context_data(self, **kwargs):
        ctx = super(ListMedidoresView, self).get_context_data(**kwargs)
        ctx['sidebar_active'] = 'medidores'
        ctx['sidebar_active_sub'] = 'listar'
        equipos = Medidor.objects.all()
        ctx['equipos'] = equipos
        return ctx