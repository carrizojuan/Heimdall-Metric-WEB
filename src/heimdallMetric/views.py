from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView
from apps.utils.mixins import AdminRequiredMixin
from apps.usuario.forms import RegisterForm, CambiarContraseñaForm, ResetPasswordForm
from apps.usuario.models import Usuario
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.shortcuts import render, redirect

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from apps.equipo.models import Equipo


class DashboardAdmin(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardAdmin, self).get_context_data(**kwargs)
        context["sidebar_active"] = "dashboard"
        equipos = Equipo.objects.all()
        context["equipos"] = equipos
        return context


def registrar_usuario(request):
    template_name = "registrarse.html"

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
    # entidad_id =
    ctx = {
        'nombre_apellido': usuario.get_full_name(),
        'nombre_usuario': usuario.nombre_usuario,
        'email': usuario.email
    }
    return render(request, template_name, ctx)


class CambiarContraseñaView(PasswordChangeView):
    template_name = "usuario/cambiar_contraseña.html"
    form_class = CambiarContraseñaForm
    success_url = reverse_lazy('dashboard_admin')


class ResetPasswordView(FormView):
    form_class = ResetPasswordForm
    template_name = 'pass_reset.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def password_reset_request(request):
    template_name = "usuario/reset_pass/password_reset.html"
    if request.method == "POST":
        password_reset_form = ResetPasswordForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            print(data)
            usuario = Usuario.objects.get(email=data)
            print(usuario)
            if usuario:
                subject = "Password Reset Requested"
                email_template_name = "usuario/reset_pass/password_reset_email.txt"
                c = {
                    "email": usuario.email,
                    "domain": "127.0.0.1:8000",
                    "site_name": "HeimdallMetric",
                    "uid": urlsafe_base64_encode(force_bytes(usuario.id)),
                    "user": usuario,
                    "token": default_token_generator.make_token(usuario),
                    "protocol": "http"
                }
                email = render_to_string(email_template_name, c)
                try:
                    send_mail(subject, email, 'admin@example.com', [usuario.email], fail_silently=False)
                except BadHeaderError:
                    return HttpResponse('Invalid header found')
                return redirect("password_reset_sent")
    password_reset_form = ResetPasswordForm()
    return render(request=request, template_name=template_name, context={"form": password_reset_form})















