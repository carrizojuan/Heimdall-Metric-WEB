from tempfile import template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from apps.utils.mixins import AdminRequiredMixin
from apps.usuario.forms import RegisterForm
from apps.usuario.models import Usuario

from django.shortcuts import render, redirect


class DashboardAdmin(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardAdmin, self).get_context_data(**kwargs)
        context["sidebar_active"] = "dashboard"
        return context


# def login(request):
#     template_name = "usuario/sign-in.html"
#     return render(request, template_name)


def registrar_usuario(request):
    template_name = "usuario/sign-up.html"

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            """ username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user) """
            return redirect('inicio')
        else:
            print("Form no valido")
    else:
        form = RegisterForm()
    return render(request, template_name, {'form': form})


def detalle_usuario(request):
    template_name = "usuario/detalle.html"
    usuario = request.user
    ctx = {
        'nombre_apellido': usuario.get_full_name(),
        'nombre_usuario': usuario.nombre_usuario,
        'correo_electronico': usuario.email
    }
    return render(request, template_name, ctx)


def lista_usuarios(request):
    template_name = "usuario/lista_usuarios.html"
    usuarios = Usuario.objects.filter(is_active=True)
    ctx = {
        'usuarios': usuarios
    }
    return render(request, template_name, ctx)
