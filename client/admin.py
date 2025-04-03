from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_num', 'address')

admin.site.register(Client, ClientAdmin)
