from django.contrib.auth.mixins import LoginRequiredMixin
from apps.utils.mixins import AdminRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .models import Medidor
from .forms import RegisterMedidorForm


class CrearMedidorView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Medidor
    template_name = 'medidor/crear_medidor.html'
    form_class = RegisterMedidorForm

    def get_success_url(self, **kwargs):
        return reverse('medidor:listar_medidores', args=[])

    def form_valid(self, form):
        f = form.save(commit=True)
        return super(CrearMedidorView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CrearMedidorView, self).get_context_data(**kwargs)
        context['sidebar_active'] = 'medidores'
        context['sidebar_active_sub'] = 'crear'
        return context


class MedidorDetalleView(LoginRequiredMixin, AdminRequiredMixin, DetailView):
    model = Medidor
    template_name = 'medidor/detalle.html'
    context_object_name = 'medidor'

    def get_context_data(self, **kwargs):
        ctx = super(MedidorDetalleView, self).get_context_data(**kwargs)
        ctx['sidebar_active'] = 'medidores'
        medidor = Medidor.objects.get(id=self.kwargs["pk"])
        ctx["medidor"] = medidor
        return ctx

class ListMedidoresView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Medidor
    template_name = "medidor/lista_medidores.html"
    context_object_name = 'medidores'

    def get_context_data(self, **kwargs):
        ctx = super(ListMedidoresView, self).get_context_data(**kwargs)
        ctx['sidebar_active'] = 'medidores'
        ctx['sidebar_active_sub'] = 'listar'
        ctx['search'] = self.request.GET.get('search', '')
        return ctx

    def get_queryset(self):
        query = Medidor.objects.all()
        search = self.request.GET.get('search', '')
        if len(search) > 0:
            query = query.filter(equipo__nro_serie__icontains=search)
        return query.order_by('equipo__nro_serie')


class EditarMedidorView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Medidor
    template_name = 'medidor/editar_medidor.html'
    form_class = RegisterMedidorForm

    def get_context_data(self, **kwargs):
        context = {}
        context['sidebar_active'] = 'medidores'
        context['form'] = RegisterMedidorForm(instance=self.object)
        # print(self.object.nro_cliente)
        equipo = Medidor.objects.get(id=self.kwargs["pk"])
        context["medidor"] = equipo
        # print(equipo)
        return context

    def form_valid(self, form):
        # print(form)
        f = form.save(commit=False)
        return super(EditarMedidorView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(EditarMedidorView, self).get_form_kwargs()
        return kwargs

    def get_success_url(self, **kw1args):
        return reverse('medidor:listar_medidores', args=[])


def eliminar_medidor(request, pk):
    medidor = Medidor.objects.get(id=pk)
    medidor.delete()
    return HttpResponseRedirect(reverse("medidor:listar_medidores"))
