from django.db import models
from users.models import User

class Service(models.Model):
    """
    Модель для создания услуги в CRM
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/service/detail/{self.id}'

class AdvertisingСompany(models.Model):
    """
    Модель для создания рекламной компании
    """
    company_name = models.CharField(max_length=255)
    advertised_service = models.ForeignKey(Service, on_delete=models.CASCADE)
    promotion_channel = models.CharField(max_length=255)
    budget = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    def __str__(self):
        return self.company_name

class Contract(models.Model):
    """
    Модель для создания контракта
    """
    name_contract = models.CharField(max_length=255)
    service_provided = models.ForeignKey(Service, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads_document')
    date_conclusion = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(auto_now_add=True)
    summ = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name_contract

class PotentialProfile(models.Model):
    """
    Модель создаёт профиль потенциального клиента
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(AdvertisingСompany, on_delete=models.CASCADE)

class ActiveProfile(models.Model):
    potential_client = models.ForeignKey(PotentialProfile, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)