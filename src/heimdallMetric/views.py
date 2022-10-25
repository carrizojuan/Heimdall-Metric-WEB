# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponseRedirect, HttpResponse
# from django.shortcuts import render, redirect
# from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from apps.utils.mixins import AdminRequiredMixin


class DashboardAdmin(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardAdmin, self).get_context_data(**kwargs)
        context["sidebar_active"] = "dashboard"
        return context
