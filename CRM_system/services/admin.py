from django.contrib import admin
from .models import Service, AdvertisingСompany, Contract, PotentialProfile, ActiveProfile

class ServiceAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name', 'description', 'price'

class AdvertisingСompanyAdmin(admin.ModelAdmin):
    list_display = 'pk', 'company_name', 'advertised_service', 'promotion_channel', 'budget'

class ContractAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name_contract', 'service_provided', 'file', 'date_conclusion', 'expiration_date', 'summ'

class PotentialProfileAdmin(admin.ModelAdmin):
    list_display = 'pk', 'user', 'company'

class ActiveProfileAdmin(admin.ModelAdmin):
    list_display = 'pk', 'potential_client', 'contract'

admin.site.register(Service, ServiceAdmin)
admin.site.register(AdvertisingСompany, AdvertisingСompanyAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(PotentialProfile, PotentialProfileAdmin)
admin.site.register(ActiveProfile, ActiveProfileAdmin)
