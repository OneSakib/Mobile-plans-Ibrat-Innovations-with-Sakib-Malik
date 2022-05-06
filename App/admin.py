from django.contrib import admin
from .models import Airtel, Vodafone, BSNL, JIO, MTNL


# Register your models here.
@admin.register(Airtel)
class AirtelAdmin(admin.ModelAdmin):
    list_display = ['id', 'plans_type', 'circle']



@admin.register(Vodafone)
class VodafoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'plans_type', 'circle']


@admin.register(BSNL)
class BSNLAdmin(admin.ModelAdmin):
    list_display = ['id', 'plans_type', 'circle']


@admin.register(JIO)
class JIOAdmin(admin.ModelAdmin):
    list_display = ['id', 'plans_type', 'circle']


@admin.register(MTNL)
class MTNLAdmin(admin.ModelAdmin):
    list_display = ['id', 'plans_type', 'circle']
