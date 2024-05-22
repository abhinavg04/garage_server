from django.db import models
from django.db.models import Sum

# Create your models here.


class CustomerCard(models.Model):
    customer=models.CharField(max_length=100)
    phone=models.IntegerField()
    vehicle_number=models.CharField(max_length=100)
    kilometeres=models.PositiveIntegerField()
    image=models.ImageField(upload_to="vehicle_images")
    status=models.CharField(max_length=100,default="pending")
    added_data=models.DateField(auto_now_add=True)

    @property
    def services(self):
        qs=Service.objects.filter(customercard=self)
        return qs
    
    @property
    def total_amount(self):
        total=self.services.values('amount').aggregate(total=Sum('amount'))['total']
        return total


class Service(models.Model):
    title=models.CharField(max_length=100)
    notes=models.CharField(max_length=500)
    amount=models.IntegerField()
    customercard=models.ForeignKey(CustomerCard,on_delete=models.CASCADE) 