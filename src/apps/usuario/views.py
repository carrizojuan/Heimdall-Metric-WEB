from django.shortcuts import render
from .models import Usuario
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.utils.mixins import AdminRequiredMixin
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

""" class EquipoInactivosView(LoginRequiredMixin, AdminRequiredMixin, ListView):
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
        return ctx """

class UsuarioAdministradorListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Usuario
    template_name = "usuario/lista_usuarios.html"

    def get_context_data(self, **kwargs):
        ctx = super(UsuarioAdministradorListView, self).get_context_data(**kwargs)
        ctx['sidebar_active'] = 'usuarios'
        ctx['usuario_status'] = 'administradores'
        usuarios = Usuario.objects.filter(is_staff=True)
        ctx['usuarios'] = usuarios
        return ctx

    
class UsuarioMonitorListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Usuario
    template_name = "usuario/lista_usuarios.html"

    def get_context_data(self, **kwargs):
        ctx = super(UsuarioMonitorListView, self).get_context_data(**kwargs)
        ctx['sidebar_active'] = 'usuarios'
        ctx['usuario_status'] = 'monitores'
        usuarios = Usuario.objects.filter(is_staff=False)
        ctx['usuarios'] = usuarios
        return ctx
    
class UsuarioInactivosListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Usuario
    template_name = "usuario/lista_usuarios.html"

    def get_context_data(self, **kwargs):
        ctx = super(UsuarioInactivosListView, self).get_context_data(**kwargs)
        ctx['sidebar_active'] = 'usuarios'
        ctx['usuario_status'] = 'inactivos'
        usuarios = Usuario.objects.filter(is_active=False)
        ctx['usuarios'] = usuarios
        return ctx
    
class UsuarioActivosListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Usuario
    template_name = "usuario/lista_usuarios.html"

    def get_context_data(self, **kwargs):
        ctx = super(UsuarioActivosListView, self).get_context_data(**kwargs)
        ctx['sidebar_active'] = 'usuarios'
        ctx['usuario_status'] = 'activos'
        usuarios = Usuario.objects.filter(is_active=True)
        ctx['usuarios'] = usuarios
        return ctx
    
class UsuarioListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Usuario
    template_name = "usuario/lista_usuarios.html"

    def get_context_data(self, **kwargs):
        ctx = super(UsuarioListView, self).get_context_data(**kwargs)
        ctx['sidebar_active'] = 'usuarios'
        ctx['usuario_status'] = 'todos'
        usuarios = Usuario.objects.all()
        ctx['usuarios'] = usuarios
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


