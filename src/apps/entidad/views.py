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
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import render, redirect
from .models import Entidad, Miembro
from .forms import RegisterEntidadForm


@login_required
def lista_entidades(request):
    template_name = "entidad/lista_entidades.html"

    entidades = Entidad.objects.all()
    ctx = {
        'entidades': entidades,
        "sidebar_active": "entidades"
    }
    return render(request, template_name, ctx)


class CrearEntidadView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Entidad
    template_name = 'entidad/nueva_entidad.html'
    form_class = RegisterEntidadForm

    def get_success_url(self, **kwargs):
        return reverse('entidad:lista_entidades', args=[])

    def form_valid(self, form):
        f = form.save(commit=True)
        return super(CrearEntidadView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CrearEntidadView, self).get_context_data(**kwargs)
        return context


class DetalleEntidadView(LoginRequiredMixin, AdminRequiredMixin, DetailView):
    model = Entidad
    template_name = 'entidad/detalle.html'
    context_object_name = 'entidad'

    def get_context_data(self, **kwargs):
        ctx = super(DetalleEntidadView, self).get_context_data(**kwargs)
        print(ctx)
        ctx['sidebar_active'] = 'entidades'
        print(kwargs.get("object").pk)
        miembros = Miembro.objects.filter(entidad=kwargs.get("object").pk)
        print(miembros)
        ctx['miembros'] = miembros
        return ctx


class ActualizarEntidadView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Entidad
    template_name = 'entidad/editar_entidad.html'
    form_class = RegisterEntidadForm

    def get_context_data(self, **kwargs):
        context = super(ActualizarEntidadView, self).get_context_data(**kwargs)
        context['sidebar_active'] = 'entidad'
        print(context)
        return context

    def get_success_url(self, **kwargs):
        return reverse('entidad:lista_entidades', args=[])

    def get_form_kwargs(self):
        kwargs = super(ActualizarEntidadView, self).get_form_kwargs()
        return kwargs


class EliminarEntidadView(DeleteView):
    model = Entidad
    success_url = reverse_lazy('entidad:lista_entidades')
    template_name = 'entidad/eliminar_entidad.html'

    def get_context_data(self, **kwargs):
        ctx = super(EliminarEntidadView, self).get_context_data(**kwargs)
        # print(self.object)
        ctx['form'] = RegisterEntidadForm(instance=self.object)
        ctx['sidebar_active'] = 'entidad'
        return ctx
