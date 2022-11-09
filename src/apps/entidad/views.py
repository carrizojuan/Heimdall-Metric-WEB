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
from apps.usuario.models import Usuario
from .forms import RegisterEntidadForm, RegisterMiembroForm


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
        # print(ctx)
        ctx['sidebar_active'] = 'entidades'
        ctx['miembro_status'] = 'todos'
        # print(kwargs.get("object").pk)
        miembros = Miembro.objects.filter(entidad=kwargs.get("object").pk)
        # print(miembros)
        ctx['miembros'] = miembros
        return ctx


class DetalleEntidadActivosView(LoginRequiredMixin, AdminRequiredMixin, DetailView):
    model = Entidad
    template_name = 'entidad/detalle.html'
    context_object_name = 'entidad'

    def get_context_data(self, **kwargs):
        ctx = super(DetalleEntidadActivosView, self).get_context_data(**kwargs)
        # print(ctx)
        ctx['sidebar_active'] = 'entidades'
        ctx['miembro_status'] = 'activos'
        # print(kwargs.get("object").pk)
        miembros = Miembro.objects.filter(entidad=kwargs.get("object").pk,activo=True)
        # print(miembros)
        ctx['miembros'] = miembros
        return ctx


class DetalleEntidadInactivosView(LoginRequiredMixin, AdminRequiredMixin, DetailView):
    model = Entidad
    template_name = 'entidad/detalle.html'
    context_object_name = 'entidad'

    def get_context_data(self, **kwargs):
        ctx = super(DetalleEntidadInactivosView, self).get_context_data(**kwargs)
        # print(ctx)
        ctx['sidebar_active'] = 'entidades'
        ctx['miembro_status'] = 'inactivos'
        # print(kwargs.get("object").pk)
        miembros = Miembro.objects.filter(entidad=kwargs.get("object").pk,activo=False)
        # print(miembros)
        ctx['miembros'] = miembros
        return ctx


class ActualizarEntidadView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Entidad
    template_name = 'entidad/editar_tipo_gateway.html'
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
    template_name = 'entidad/eliminar_tipo_gateway.html'

    def get_context_data(self, **kwargs):
        ctx = super(EliminarEntidadView, self).get_context_data(**kwargs)
        # print(self.object)
        ctx['form'] = RegisterEntidadForm(instance=self.object)
        ctx['sidebar_active'] = 'entidad'
        return ctx


class CrearMiembroView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Miembro
    template_name = 'entidad/miembro/nuevo_miembro.html'
    form_class = RegisterMiembroForm

    def get_success_url(self, **kwargs):
        return reverse('entidad:detalle_entidad', kwargs={'pk': self.kwargs.get("pk")})

    def form_valid(self, form):
        f = form.save(commit=False)
        # print(form)
        f.entidad = Entidad.objects.get(id=self.kwargs["pk"])
        return super(CrearMiembroView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CrearMiembroView, self).get_context_data(**kwargs)
        context["entidad"] = self.kwargs["pk"]
        entidades = Entidad.objects.filter(id=self.kwargs["pk"])
        # print(entidades)
        miembros_entidad = Miembro.objects.filter(entidad=self.kwargs["pk"]).values('usuario__pk')
        # print(miembros_entidad)
        context["form"].fields["usuario"].queryset = Usuario.objects.exclude(pk__in=miembros_entidad)
        # print(context)
        return context


class EliminarMiembroView(DeleteView):
    model = Miembro
    success_url = reverse_lazy('entidad:lista_entidades')
    template_name = 'entidad/miembro/eliminar_miembro.html'

    def get_context_data(self, **kwargs):
        ctx = super(EliminarMiembroView, self).get_context_data(**kwargs)
        # print(self.object)
        ctx['form'] = RegisterMiembroForm(instance=self.object)
        ctx['form'].fields["usuario"].widget.attrs["disabled"] = True
        ctx['form'].fields["rol"].widget.attrs["disabled"] = True
        ctx['form'].fields["activo"].widget.attrs["disabled"] = True
        ctx['sidebar_active'] = 'entidades'
        return ctx


class ActualizarMiembroView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Miembro
    template_name = 'entidad/miembro/editar_miembro.html'
    form_class = RegisterMiembroForm

    def get_context_data(self, **kwargs):
        context = super(ActualizarMiembroView, self).get_context_data(**kwargs)
        context["miembro"] = self.kwargs["pk"]
        miembro = Miembro.objects.get(pk=self.kwargs["pk"])
        entidad = Entidad.objects.get(id=miembro.entidad.pk)
        context["entidad"] = entidad
        context['form'].fields["usuario"].widget.attrs["readonly"] = True
        return context

    def get_success_url(self, **kwargs):
        miembro = Miembro.objects.get(pk=self.kwargs["pk"])
        return reverse('entidad:detalle_entidad', kwargs={'pk': miembro.entidad.pk})

    def get_form_kwargs(self):
        kwargs = super(ActualizarMiembroView, self).get_form_kwargs()
        return kwargs
