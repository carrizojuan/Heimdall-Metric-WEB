from django.shortcuts import render
from .models import Usuario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

class UsuarioAdministradorListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = "usuario/usuarios_administrador.html"

    def get_queryset(self):
        queryset = self.model.objects.filter(is_staff=True)
        return queryset

    def get_context_data(self, **kwargs):
        ctx = super(UsuarioAdministradorListView, self).get_context_data(**kwargs)
        ctx['sidebar_active_usuarios'] = 'administradores'
        ctx['sidebar_active'] = 'usuarios'
        return ctx

    
class UsuarioMonitorListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = "usuario/usuarios_monitor.html"

    def get_queryset(self):
        queryset = self.model.objects.filter(is_staff=False)
        return queryset

    def get_context_data(self, **kwargs):
        ctx = super(UsuarioMonitorListView, self).get_context_data(**kwargs)
        ctx['sidebar_active_usuarios'] = 'monitores'
        ctx['sidebar_active'] = 'usuarios'
        return ctx
    
class UsuarioInactivosListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = "usuario/usuarios_inactivos.html"

    def get_queryset(self):
        queryset = self.model.objects.filter(is_active=False)
        return queryset

    def get_context_data(self, **kwargs):
        ctx = super(UsuarioInactivosListView, self).get_context_data(**kwargs)
        ctx['sidebar_active_usuarios'] = 'inactivos'
        ctx['sidebar_active'] = 'usuarios'
        return ctx
    
class UsuarioActivosListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = "usuario/usuarios_activos.html"

    def get_queryset(self):
        queryset = self.model.objects.filter(is_active=True)
        return queryset

    def get_context_data(self, **kwargs):
        ctx = super(UsuarioActivosListView, self).get_context_data(**kwargs)
        ctx['sidebar_active_usuarios'] = 'activos'
        ctx['sidebar_active'] = 'usuarios'
        return ctx
    
class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = "usuario/usuarios.html"

    def get_context_data(self, **kwargs):
        ctx = super(UsuarioListView, self).get_context_data(**kwargs)
        ctx['sidebar_active_usuarios'] = 'todos'
        ctx['sidebar_active'] = 'usuarios'
        return ctx
    


def inactivar_usuario(request, id):
    user = Usuario.objects.get(id = id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse("usuario:usuarios_activos"))

def activar_usuario(request, id):
    user = Usuario.objects.get(id = id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse("usuario:usuarios_inactivos"))


