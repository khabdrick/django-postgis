from django.contrib import admin
from .models import LonLat, Road, Country
from django.contrib.gis.admin import OSMGeoAdmin

@admin.register(LonLat)
class LonLatAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')

@admin.register(Road)
class RoadsAdmin(OSMGeoAdmin):
    list_display = ('name', 'path')

@admin.register(Country)
class CountriesAdmin(OSMGeoAdmin):
    list_display = ('name', 'area')