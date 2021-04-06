from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView




class Index(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        
        context = {
        }

        return self.render_to_response(context)


class Application(TemplateView):
    template_name = 'application.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        
        context = {
        }

        return self.render_to_response(context)
