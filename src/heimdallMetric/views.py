from tempfile import template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from apps.utils.mixins import AdminRequiredMixin
from apps.usuario.forms import RegisterForm, CambiarContraseñaForm, ResetPasswordForm
from apps.usuario.models import Usuario
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect


class DashboardAdmin(LoginRequiredMixin,TemplateView):
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
    #entidad_id = 
    ctx = {
        'nombre_apellido': usuario.get_full_name(),
        'nombre_usuario': usuario.nombre_usuario,
        'email': usuario.email
    }
    return render(request, template_name, ctx)


@login_required
def lista_usuarios(request):
    template_name = "usuario/lista_usuarios.html"

    usuarios = Usuario.objects.filter(is_active=True)
    ctx = {
        'usuarios': usuarios,
        "sidebar_active": "usuarios"
    }
    return render(request, template_name, ctx)



class CambiarContraseñaView(PasswordChangeView):
    template_name = "usuario/cambiar_contraseña.html"
    form_class = CambiarContraseñaForm
    success_url = reverse_lazy('dashboard_admin')



class ResetPasswordView(FormView):
    form_class = ResetPasswordForm
    template_name = 'usuario/forgot-password.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
