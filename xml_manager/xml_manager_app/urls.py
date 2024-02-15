from django.urls import path, include
from .views import MainView, ServicesToServedView, AllServicesView, ServedServicesView, ServiceDetailsView

urlpatterns = [
    path("", MainView.as_view(), name="main_view"),
    path("services_to_served/", ServicesToServedView.as_view(), name="services_to_served"),
    path("services_served/", ServedServicesView.as_view(), name="services_served"),
    path("services_all/", AllServicesView.as_view(), name="services_all"),
    path("service_details/", ServiceDetailsView.as_view(), name="service_details"),
]
