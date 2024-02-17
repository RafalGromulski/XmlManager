from django.urls import path

from .views import MainView, ServicesToServedView, ServedServicesView, AllServicesView, ServiceDetailsView, ConfirmServiceView, CrlUrlModifyView

urlpatterns = [
    path("", MainView.as_view(), name="main_view"),
    path("services_to_served/", ServicesToServedView.as_view(), name="services_to_served"),
    path("services_served/", ServedServicesView.as_view(), name="services_served"),
    path("services_all/", AllServicesView.as_view(), name="services_all"),
    path("service_details/<pk>/", ServiceDetailsView.as_view(), name="service_details"),
    path("confirm_service/<int:pk>/", ConfirmServiceView.as_view(), name="confirm_service"),
    path("crl_url_modify/<int:pk>/", CrlUrlModifyView.as_view(), name="crl_url_modify"),
]
