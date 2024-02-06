# from django.shortcuts import render
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = "main_view.html"


class ServicesToServedView(TemplateView):
    template_name = "services_to_served.html"


class AllServicesView(TemplateView):
    template_name = "services_all.html"


class ServedServicesView(TemplateView):
    template_name = "services_served.html"


class ServiceDetailsView(TemplateView):
    template_name = "service_details.html"

