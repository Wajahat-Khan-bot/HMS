from django.contrib import admin
from .models import Asset


class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_num', 'address', 'sitee')


admin.site.register(Asset, AssetAdmin)
