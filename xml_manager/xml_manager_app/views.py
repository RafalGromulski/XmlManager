from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.generic import DetailView, TemplateView, View, UpdateView

from .filters import DataFilter
from .forms import CrlUrlModify
from .models import TspServiceDetails


class MainView(TemplateView):
    template_name = "main_view.html"


class ServicesToServedView(LoginRequiredMixin, View):
    template_name = "services_to_served.html"
    model = TspServiceDetails

    def get(self, request):
        services_to_served = self.model.objects.filter(
            Q(service_status_app="Not served (new)") | Q(service_status_app="Not served (withdraw)")
        ).order_by("country_name", "tsp_name", "service_name", "id")
        data_filter = DataFilter(request.GET, queryset=services_to_served)
        services_to_served = data_filter.qs
        context = {
            "services_to_served": services_to_served,
            "data_filter": data_filter,
        }
        return render(request, self.template_name, context)


class ServedServicesView(View):
    template_name = "services_served.html"
    model = TspServiceDetails

    def get(self, request):
        services_served = self.model.objects.filter(service_status_app="Served").order_by(
            "id", "country_name", "tsp_name"
        )
        data_filter = DataFilter(request.GET, queryset=services_served)
        served_services = data_filter.qs
        context = {
            "served_services": served_services,
            "data_filter": data_filter,
        }
        return render(request, self.template_name, context)


class AllServicesView(View):
    template_name = "services_all.html"
    model = TspServiceDetails

    def get(self, request):
        services_all = self.model.objects.all()
        data_filter = DataFilter(request.GET, queryset=services_all)
        all_services = data_filter.qs
        context = {
            "all_services": all_services,
            "data_filter": data_filter,
        }
        return render(request, self.template_name, context)


class ServiceDetailsView(LoginRequiredMixin, DetailView):
    template_name = "service_details.html"
    model = TspServiceDetails
    context_object_name = "trust_service"


class ConfirmServiceView(LoginRequiredMixin, View):
    model = TspServiceDetails
    template_name = "confirm_service.html"

    def get(self, request, pk):
        tsp_object = self.model.objects.get(pk=pk)
        context = {"tsp_object": tsp_object}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        tsp_object = self.model.objects.get(pk=pk)
        tsp_object.service_status_app = "Served"
        tsp_object.save()
        return redirect("services_to_served")


class CrlUrlModifyView(LoginRequiredMixin, UpdateView):
    model = TspServiceDetails
    template_name = "crl_url_modify.html"
    form_class = CrlUrlModify
    success_url = "/services_to_served/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tsp_object"] = self.model.objects.get(id=self.kwargs["pk"])
        return context

    def get_initial(self):
        initial = super().get_initial()
        initial["crl_url"] = self.model.objects.get(id=self.kwargs["pk"]).crl_url
        return initial

    def form_valid(self, form):
        self.object.service_status_app = "Served"
        self.object.crl_url_status_app = "CRL URL determined"
        form.save()
        return super().form_valid(form)
