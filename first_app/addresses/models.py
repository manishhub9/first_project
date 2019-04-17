from django.db import models
from billing.models import BillingProfile


ADDRESS_TYPE = (
        ('billig',"Billing"),
        ('shipping',"Shipping")
)

class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile)
    address_type = models.CharField(max_length=120, choices=ADDRESS_TYPE)
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(max_length=200, null=True,blank=True)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=120)

    def __str__(self):
        return str(self.billing_profile)
