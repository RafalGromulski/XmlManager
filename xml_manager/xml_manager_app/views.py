from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, View

from .models import TspServiceDetails


class MainView(TemplateView):
    template_name = "main_view.html"


class ServicesToServedView(View):
    template_name = "services_to_served.html"
    model = TspServiceDetails

    def get(self, request):
        services_to_served = self.model.objects.filter(
            Q(service_status_app="Not served (new)") | Q(service_status_app="Not served (withdraw)")
        ).order_by("country_name", "tsp_name", "service_name", "id")
        context = {
            "services_to_served": services_to_served,
        }
        return render(request, self.template_name, context)


class AllServicesView(View):
    template_name = "services_all.html"
    model = TspServiceDetails

    def get(self, request):
        all_services = self.model.objects.all()
        context = {
            "all_services": all_services,
        }
        return render(request, self.template_name, context)


class ServedServicesView(View):
    template_name = "services_served.html"
    model = TspServiceDetails

    def get(self, request):
        served_services = self.model.objects.filter(service_status_app="Served").order_by(
            "id", "country_name", "tsp_name"
        )
        context = {
            "served_services": served_services,
        }
        return render(request, self.template_name, context)


class ServiceDetailsView(TemplateView):
    template_name = "service_details.html"
