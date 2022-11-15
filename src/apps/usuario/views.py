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
    context_object_name = 'usuarios'

    def get_context_data(self, **kwargs):
        ctx = super(UsuarioAdministradorListView, self).get_context_data(**kwargs)
        ctx['sidebar_active'] = 'usuarios'
        ctx['usuario_status'] = 'administradores'
        return ctx

    def get_queryset(self):
        query = Usuario.objects.filter(is_staff=True)
        search = self.request.GET.get('search', '')
        if len(search) > 0:
            query = query.filter(apellidos__icontains=search)
        return query.order_by('apellidos')


class UsuarioMonitorListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Usuario
    template_name = "usuario/lista_usuarios.html"
    context_object_name = 'usuarios'

    def get_context_data(self, **kwargs):
        ctx = super(UsuarioMonitorListView, self).get_context_data(**kwargs)
        ctx['sidebar_active'] = 'usuarios'
        ctx['usuario_status'] = 'monitores'
        return ctx
    
    def get_queryset(self):
        query = Usuario.objects.filter(is_staff=False)
        search = self.request.GET.get('search', '')
        if len(search) > 0:
            query = query.filter(apellidos__icontains=search)
        return query.order_by('apellidos')


class UsuarioInactivosListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Usuario
    template_name = "usuario/lista_usuarios.html"
    context_object_name = 'usuarios'

    def get_context_data(self, **kwargs):
        ctx = super(UsuarioInactivosListView, self).get_context_data(**kwargs)
        ctx['sidebar_active'] = 'usuarios'
        ctx['usuario_status'] = 'inactivos'
        return ctx

    def get_queryset(self):
        query = Usuario.objects.filter(is_active=False)
        search = self.request.GET.get('search', '')
        if len(search) > 0:
            query = query.filter(apellidos__icontains=search)
        return query.order_by('apellidos')


class UsuarioActivosListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Usuario
    template_name = "usuario/lista_usuarios.html"
    context_object_name = 'usuarios'

    def get_context_data(self, **kwargs):
        ctx = super(UsuarioActivosListView, self).get_context_data(**kwargs)
        ctx['sidebar_active'] = 'usuarios'
        ctx['usuario_status'] = 'activos'
        return ctx

    def get_queryset(self):
        query = Usuario.objects.filter(is_active=True)
        search = self.request.GET.get('search', '')
        if len(search) > 0:
            query = query.filter(apellidos__icontains=search)
        return query.order_by('apellidos')


class UsuarioListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Usuario
    template_name = "usuario/lista_usuarios.html"
    context_object_name = 'usuarios'

    def get_context_data(self, **kwargs):
        ctx = super(UsuarioListView, self).get_context_data(**kwargs)
        ctx['sidebar_active'] = 'usuarios'
        ctx['usuario_status'] = 'todos'
        ctx['search'] = self.request.GET.get('search', '')
        return ctx

    def get_queryset(self):
        query = Usuario.objects.all()
        search = self.request.GET.get('search', '')
        if len(search) > 0:
            query = query.filter(apellidos__icontains=search)
        return query.order_by('apellidos')


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


