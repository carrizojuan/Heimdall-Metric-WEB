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
from .models import TipoGateway, Consola
from .forms import RegisterTipoGatewayForm, DetalleConsolaForm


class TiposGatewayView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    template_name = 'tipo_gateway/lista_tipos_gateways.html'
    model = TipoGateway
    context_object_name = "gateways"
    # paginate_by = 20

    def get_context_data(self, **kwargs):
        ctx = super(TiposGatewayView, self).get_context_data(**kwargs)
        ctx['sidebar_active'] = 'tipo_gateway'
        return ctx


class CrearTipoGatewayView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = TipoGateway
    template_name = 'tipo_gateway/nuevo_tipo_gateway.html'
    form_class = RegisterTipoGatewayForm

    def get_success_url(self, **kwargs):
        return reverse('tipo_gateway:lista_tipogateway', args=[])

    def form_valid(self, form):
        f = form.save(commit=True)
        return super(CrearTipoGatewayView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CrearTipoGatewayView, self).get_context_data(**kwargs)
        return context


class DetalleTipoGatewayView(LoginRequiredMixin, AdminRequiredMixin, DetailView):
    model = TipoGateway
    template_name = 'tipo_gateway/detalle.html'
    context_object_name = 'tipo_gateway'

    def get_context_data(self, **kwargs):
        ctx = super(DetalleTipoGatewayView, self).get_context_data(**kwargs)
        # print(ctx)
        ctx['sidebar_active'] = 'tipo_gateway'
        consolas = Consola.objects.filter(tipo_gateway=kwargs.get("object").pk)
        # print(miembros)
        ctx['consolas'] = consolas

        return ctx


class ActualizarTipoGatewayView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = TipoGateway
    template_name = 'tipo_gateway/editar_tipo_gateway.html'
    form_class = RegisterTipoGatewayForm
    context_object_name = 'tipo_gateway'

    def get_context_data(self, **kwargs):
        context = super(ActualizarTipoGatewayView, self).get_context_data(**kwargs)
        context['sidebar_active'] = 'tipo_gateway'
        # print(context)
        return context

    def get_success_url(self, **kwargs):
        return reverse('tipo_gateway:lista_tipogateway', args=[])

    def get_form_kwargs(self):
        kwargs = super(ActualizarTipoGatewayView, self).get_form_kwargs()
        return kwargs


class EliminarTipoGatewayView(DeleteView):
    model = TipoGateway
    success_url = reverse_lazy('tipo_gateway:lista_tipogateway')
    template_name = 'tipo_gateway/eliminar_tipo_gateway.html'
    context_object_name = 'tipo_gateway'

    def get_context_data(self, **kwargs):
        ctx = super(EliminarTipoGatewayView, self).get_context_data(**kwargs)
        # print(self.object)
        ctx['form'] = RegisterTipoGatewayForm(instance=self.object)
        ctx['sidebar_active'] = 'tipo_gateway'
        return ctx


class EliminarConsolaView(DeleteView):
    model = Consola
    success_url = reverse_lazy('tipo_gateway:lista_tipogateway')
    template_name = 'tipo_gateway/consola/eliminar_consola.html'

    def get_context_data(self, **kwargs):
        ctx = super(EliminarConsolaView, self).get_context_data(**kwargs)
        # print(self.object)
        ctx['form'] = DetalleConsolaForm(instance=self.object)
        ctx["tipo_gateway"] = self.object.tipo_gateway
        # ctx['form'].fields["usuario"].widget.attrs["disabled"] = True
        # ctx['form'].fields["rol"].widget.attrs["disabled"] = True
        # ctx['form'].fields["activo"].widget.attrs["disabled"] = True
        ctx['sidebar_active'] = 'tipo_gateway'
        return ctx



