# from tempfile import template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
# from django.views.generic import TemplateView, FormView
from apps.utils.mixins import AdminRequiredMixin
# from django.contrib import messages
# from django.contrib.auth import update_session_auth_hash
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import render, redirect
from .models import TipoGateway
# from .forms import RegisterTipoGateway


class TiposGatewayView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    template_name = 'tipo_gateway/lista_tipos_gateways.html'
    model = TipoGateway
    context_object_name = "gateways"
    # paginate_by = 20

    def get_context_data(self, **kwargs):
        ctx = super(TiposGatewayView, self).get_context_data(**kwargs)
        ctx['sidebar_active'] = 'tipo_gateway'
        return ctx
