from django.contrib import admin
from .models import Sitee

class SiteeAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_num', 'customer')

admin.site.register(Sitee, SiteeAdmin)
