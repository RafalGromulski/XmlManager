from django.db import models


class TslValidityInfo(models.Model):
    country_code = models.CharField(verbose_name="Kod państwa", max_length=2)
    country_name = models.CharField(verbose_name="Państwo", max_length=20)
    tsl_operator_name = models.CharField(verbose_name="Nazwa operatora TSL", max_length=255)
    tsl_issue_date = models.DateTimeField(verbose_name="Data wydania TSL")
    tsl_expiry_date = models.DateTimeField(verbose_name="Data ważności TSL")
    tsl_validity_alert = models.CharField(verbose_name="Status TSL", max_length=100, default="")

    def __str__(self):
        return "Country: " + str(self.country_name) + " — TSL Operator Name: " + str(self.tsl_operator_name)
