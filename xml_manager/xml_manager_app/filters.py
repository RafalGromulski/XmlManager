from django_filters import AllValuesFilter, CharFilter, ChoiceFilter, FilterSet

from .models import TspServiceDetails


class DataFilter(FilterSet):
    country_name = AllValuesFilter(
        empty_label="Country..."
    )

    tsp_name = CharFilter(
        label="Trust service provider...",
        lookup_expr="icontains"
    )

    service_name = CharFilter(
        label="Service name...",
        lookup_expr="icontains"
    )

    crl_url_status_app = ChoiceFilter(
        empty_label="CRL URL status...",
        choices=TspServiceDetails.CrlUrlStatus.choices,
    )

    service_status = ChoiceFilter(
        empty_label="Service status...",
        choices=TspServiceDetails.TspServiceStatus.choices,
    )

    service_type = AllValuesFilter(
        empty_label="Service type...",
    )

    service_status_app = ChoiceFilter(
        empty_label="Status in XML Manager...",
        choices=TspServiceDetails.ServiceStatus.choices,
    )

    class Meta:
        model = TspServiceDetails
        fields = []
