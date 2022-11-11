from django.contrib.auth.mixins import LoginRequiredMixin
from apps.utils.mixins import AdminRequiredMixin
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Equipo
from .forms import RegisterEquipoForm

class CrearEquipoView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Equipo
    template_name = 'equipo/crear_equipo.html'
    form_class = RegisterEquipoForm

    def get_success_url(self, **kwargs):
        return reverse('equipo:listar_equipos', args=[])

    def form_valid(self, form):
        f = form.save(commit=True)
        return super(CrearEquipoView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CrearEquipoView, self).get_context_data(**kwargs)
        return context

    
class ListEquiposView(LoginRequiredMixin, AdminRequiredMixin, ListView):

    model = Equipo
    template_name = "equipo/lista_equipos.html"

    def get_context_data(self, **kwargs):
        ctx = super(ListEquiposView, self).get_context_data(**kwargs)
        ctx['sidebar_active'] = 'equipos'
        return ctx


def eliminar_equipo(request, nro_serie):
    print(nro_serie)
    equipo = Equipo.objects.get(nro_serie = nro_serie)
    equipo.delete()
    return HttpResponseRedirect(reverse("equipo:listar_equipos"))


class EquipoInactivosListView(LoginRequiredMixin, ListView):
    model = Equipo
    template_name = "equipo/equipos_inactivos.html"

    def get_queryset(self):
        queryset = self.model.objects.filter(activo=False)
        return queryset

    def get_context_data(self, **kwargs):
        ctx = super(EquipoInactivosListView, self).get_context_data(**kwargs)
        ctx['sidebar_active_equipos'] = 'inactivos'
        ctx['sidebar_active'] = 'equipos'
        return ctx
    
class EquipoActivosListView(LoginRequiredMixin, ListView):
    model = Equipo
    template_name = "equipo/equipos_activos.html"

    def get_queryset(self):
        queryset = self.model.objects.filter(activo=True)
        return queryset

    def get_context_data(self, **kwargs):
        ctx = super(EquipoActivosListView, self).get_context_data(**kwargs)
        ctx['sidebar_active_equipos'] = 'activos'
        ctx['sidebar_active'] = 'equipos'
        return ctx
    

class EquipoDetalleView(LoginRequiredMixin, AdminRequiredMixin, DetailView):
    model = Equipo
    template_name = 'equipo/detalle.html'
    context_object_name = 'equipo'

    def get_context_data(self, **kwargs):
        ctx = super(EquipoDetalleView, self).get_context_data(**kwargs)
        ctx['sidebar_active'] = 'equipos'
        equipo = Equipo.objects.get(nro_serie=self.kwargs["pk"])
        ctx["equipo"] = equipo
        return ctx