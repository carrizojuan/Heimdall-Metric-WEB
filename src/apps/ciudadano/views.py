# from tempfile import template
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
# from django.views.generic import TemplateView, FormView
from apps.utils.mixins import AdminRequiredMixin
# from django.contrib import messages
# from django.contrib.auth import update_session_auth_hash
# from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView
from apps.ciudadano.models import AuthUsuario
from apps.medidor.models import Medidor
from .forms import CiudadanoForm, DetalleCiudadanoForm
import logging


logger = logging.getLogger(__name__)

class CiudadanosView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    template_name = "ciudadano/lista_ciudadanos.html"
    model = AuthUsuario
    context_object_name = "ciudadanos"
    # paginate_by = 20

    def get_context_data(self, **kwargs):
        ctx = super(CiudadanosView, self).get_context_data(**kwargs)
        ctx['search'] = self.request.GET.get('search', '')
        ctx['sidebar_active'] = 'ciudadanos'
        ctx['sidebar_active_sub'] = 'listar_ciudadanos'
        return ctx

    def get_queryset(self):
        query = AuthUsuario.objects.using('api').all()
        search = self.request.GET.get('search', '')
        if len(search) > 0:
            query = query.filter(apellidos__icontains=search)
        return query.order_by('apellidos')


class DetalleCiudadanoView(LoginRequiredMixin, AdminRequiredMixin, DetailView):
    # model = AuthUsuario
    template_name = 'ciudadano/detalle.html'
    context_object_name = 'ciudadano'
    form_class = CiudadanoForm

    def get_context_data(self, **kwargs):
        ctx = super(DetalleCiudadanoView, self).get_context_data(**kwargs)
        ctx['sidebar_active'] = 'ciudadanos'
        ciudadano = AuthUsuario.objects.using('api').get(nro_cliente=kwargs.get("object").pk)
        ctx['medidores'] = Medidor.objects.filter(nro_cliente=ciudadano.nro_cliente)
        ctx['search'] = self.request.GET.get('search', '')
        ctx['form'] = DetalleCiudadanoForm(instance=self.object)
        print(ctx)
        return ctx

    def get_queryset(self):
        query = AuthUsuario.objects.using('api').all()
        return query


class ActualizarCiudadanoView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    template_name = 'ciudadano/editar_ciudadano.html'
    form_class = CiudadanoForm
    context_object_name = 'ciudadano'

    def get_context_data(self, **kwargs):
        context = super(ActualizarCiudadanoView, self).get_context_data(**kwargs)
        context['sidebar_active'] = 'ciudadano'
        # print(context)
        return context

    def get_success_url(self, **kwargs):
        return reverse('ciudadano:lista_ciudadano', args=[])

    def get_form_kwargs(self):
        kwargs = super(ActualizarCiudadanoView, self).get_form_kwargs()
        return kwargs

    def get_queryset(self):
        query = AuthUsuario.objects.using('api').filter(nro_cliente=self.kwargs.get("pk"))
        # print(query)
        return query

    def form_valid(self, form):
        print(self,form)
        f = form.save(commit=False)
        ciudadano = AuthUsuario.objects.using('api').get(id=form.instance.id)
        ciudadano.nombres = form.instance.nombres
        ciudadano.nombres = form.instance.apellidos
        ciudadano.nombres = form.instance.nombre_usuario
        ciudadano.nombres = form.instance.email
        ciudadano.save()
        print(f,ciudadano)
        return super(ActualizarCiudadanoView, self).form_valid(form)
