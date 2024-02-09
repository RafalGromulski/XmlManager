from django.db import models
from django.utils.translation import gettext_lazy as _


class TspServiceDetails(models.Model):
    class TspServiceStatus(models.TextChoices):
        GRANTED = "Granted"
        WITHDRAWN = "Withdrawn"

    class ServiceStatus(models.TextChoices):
        NEW_NOT_SERVED = "Nie obsłużona (nowa)", _("Nie obsłużona (nowa)")
        WITHDRAWN_NOT_SERVED = "Nie obsłużona (wycofana)", _("Nie obsłużona (wycofana)")
        SERVED = "Obsłużona", _("Obsłużona")

    class CrlUrlStatus(models.TextChoices):
        URL_DEFINED = "CRL URL ustalony", _("CRL URL ustalony")
        URL_UNDEFINED = "CRL URL nieustalony", _("CRL URL nieustalony")

    country_code = models.CharField(verbose_name="Kod państwa", max_length=2)
    country_name = models.CharField(verbose_name="Państwo", max_length=20)
    tsp_name = models.CharField(verbose_name="Dostawca usługi", max_length=255)
    service_name = models.CharField(verbose_name="Nazwa usługi", max_length=255)
    service_status = models.CharField(verbose_name="Status usługi", max_length=50, choices=TspServiceStatus.choices)
    service_start_date = models.DateTimeField(verbose_name="Start usługi")
    tsp_url = models.CharField(verbose_name="TSP URL", max_length=150, default="")
    crl_url = models.URLField(verbose_name="CRL URL", max_length=150, default="")
    crl_url_status_app = models.CharField(verbose_name="Status CRL URL", max_length=50, choices=CrlUrlStatus.choices)
    service_type = models.CharField(verbose_name="Typ usługi", max_length=100, default="")
    service_status_app = models.CharField(
        verbose_name="Status obsługi",
        max_length=100,
        choices=ServiceStatus.choices,
    )
    service_digital_id = models.TextField(verbose_name="ID usługi", default="")

    def __str__(self):
        return "TSP: " + str(self.tsp_name) + " — Service: " + str(self.service_name)
