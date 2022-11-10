from django.contrib.auth.mixins import LoginRequiredMixin
from apps.utils.mixins import AdminRequiredMixin
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.urls import reverse
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
        ctx['sidebar_active_usuarios'] = 'todos'
        ctx['sidebar_active'] = 'usuarios'
        return ctx