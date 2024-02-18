from django.db import models
from django.utils.translation import gettext_lazy as _


class TspServiceDetails(models.Model):
    class TspServiceStatus(models.TextChoices):
        GRANTED = "Granted"
        WITHDRAWN = "Withdrawn"

    class ServiceStatus(models.TextChoices):
        NOT_SERVED_NEW = "Not served (new)", _("Not served (new)")
        NOT_SERVED_WITHDRAWN = "Not served (withdrawn)", _("Not served (withdrawn)")
        SERVED = "Served", _("Served")

    class CrlUrlStatus(models.TextChoices):
        URL_DETERMINED = "CRL URL determined", _("CRL URL determined")
        URL_UNDETERMINED = "CRL URL undetermined", _("CRL URL undetermined")

    country_code = models.CharField(verbose_name="Country code", max_length=2)
    country_name = models.CharField(verbose_name="Country", max_length=20)
    tsp_name = models.CharField(verbose_name="Trust service provider", max_length=255)
    service_name = models.CharField(verbose_name="Service name", max_length=255)
    service_status = models.CharField(verbose_name="Service status", max_length=50, choices=TspServiceStatus.choices)
    service_start_date = models.DateTimeField(verbose_name="Service start date")
    tsp_url = models.CharField(verbose_name="TSP URL", max_length=150, default="")
    crl_url = models.URLField(verbose_name="CRL URL", max_length=150, default="")
    crl_url_status_app = models.CharField(verbose_name="CRL URL status", max_length=50, choices=CrlUrlStatus.choices)
    service_type = models.CharField(verbose_name="Service type", max_length=100, default="")
    service_status_app = models.CharField(
        verbose_name="Status in Xml Manager",
        max_length=100,
        choices=ServiceStatus.choices,
    )
    service_digital_id = models.TextField(verbose_name="Digital ID", default="")

    def __str__(self):
        return "TSP: " + str(self.tsp_name) + " — Service: " + str(self.service_name)
