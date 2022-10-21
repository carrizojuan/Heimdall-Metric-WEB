
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from apps.utils.mixins import AdminRequiredMixin
from apps.usuario.forms import RegisterForm

from django.shortcuts import render

class DashboardAdmin(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardAdmin, self).get_context_data(**kwargs)
        context["sidebar_active"] = "dashboard"
        return context


def login(request):
    template_name = "usuario/sign-in.html"
    return render(request, template_name)


def registrar_usuario(request):
    template_name = "usuario/sign-up.html"
    form = RegisterForm()
    return render(request, template_name, {'form': form})