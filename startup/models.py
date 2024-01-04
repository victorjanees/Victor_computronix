from django.db import models

class Raise_request(models.Model):
    customer_name = models.CharField(max_length = 20)
    customer_mobile_number = models.CharField(max_length = 10)
    service_you_need = models.CharField(max_length = 20)
    details_of_it = models.CharField(max_length = 255,blank=True)