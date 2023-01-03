from django.contrib.auth.mixins import LoginRequiredMixin
from apps.utils.mixins import AdminRequiredMixin
# from django import forms
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Equipo
from .forms import RegisterEquipoForm, EditEquipoForm
from django.http import JsonResponse




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
    context_object_name = 'equipos'

    def get_context_data(self, **kwargs):
        ctx = super(ListEquiposView, self).get_context_data(**kwargs)
        ctx['sidebar_active'] = 'equipos'
        ctx['equipo_status'] = 'todos'
        ctx['search'] = self.request.GET.get('search', '')
        return ctx

    def get_queryset(self):
        query = Equipo.objects.all()
        search = self.request.GET.get('search', '')
        if len(search) > 0:
            query = query.filter(nro_serie__icontains=search)
        return query.order_by('nro_serie')

def eliminar_equipo(request, nro_serie):
    equipo = Equipo.objects.get(nro_serie = nro_serie)
    equipo.delete()
    return HttpResponseRedirect(reverse("equipo:listar_equipos"))

class EquipoActivosView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Equipo
    template_name = 'equipo/lista_equipos.html'
    context_object_name = 'equipo'

    def get_context_data(self, **kwargs):
        ctx = super(EquipoActivosView, self).get_context_data(**kwargs)
        ctx['sidebar_active'] = 'equipos'
        ctx['equipo_status'] = 'activos'
        equipos = Equipo.objects.filter(activo=True)
        ctx['equipos'] = equipos
        return ctx


class EquipoInactivosView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Equipo
    template_name = 'equipo/lista_equipos.html'
    context_object_name = 'equipo'

    def get_context_data(self, **kwargs):
        ctx = super(EquipoInactivosView, self).get_context_data(**kwargs)
        # print(ctx)
        ctx['sidebar_active'] = 'equipos'
        ctx['equipo_status'] = 'inactivos'
        equipos = Equipo.objects.filter(activo=False)
        ctx['equipos'] = equipos
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


class ActualizarEquipoView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Equipo
    template_name = 'equipo/editar_equipo.html'
    form_class = EditEquipoForm

    def get_context_data(self, **kwargs):
        context = super(ActualizarEquipoView, self).get_context_data(**kwargs)
        context['sidebar_active'] = 'equipos'
        equipo = Equipo.objects.get(nro_serie=self.kwargs["pk"])
        context["equipo"] = equipo
        return context

    def get_success_url(self):
        return reverse('equipo:equipo_detalle', args=[self.kwargs["pk"]])

    def form_valid(self, form):
        f = form.save(commit=True)
        return super(ActualizarEquipoView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(ActualizarEquipoView, self).get_form_kwargs()
        return kwargs

#API PARA MOSTRAR LOS EQUIPOS EN EL MAPA

def api_equipos(request):
    equipos = Equipo.objects.filter(activo=True)
    data = [{'latitud': equipo.latitud, 'longitud': equipo.longitud, 'activo': equipo.activo} for equipo in equipos]
    return JsonResponse(data, safe=False)