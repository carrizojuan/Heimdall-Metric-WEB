# from tempfile import template
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
# from django.urls import reverse, reverse_lazy
# from django.views.generic import TemplateView, FormView
from apps.utils.mixins import AdminRequiredMixin
# from django.contrib import messages
# from django.contrib.auth import update_session_auth_hash
# from django.views.generic.edit import CreateView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView
from apps.ciudadano.models import AuthUsuario


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
