from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name="index.html"

class AboutView(TemplateView):
    template_name="about.html"

class ServiceView(TemplateView):
    template_name="services.html"

class BlogsView(TemplateView):
    template_name="blogs.html"

class ContactView(TemplateView):
    template_name="contact.html"






