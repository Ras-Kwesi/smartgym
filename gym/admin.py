from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from django.contrib.gis.admin import GeoModelAdmin
from .models import Gym


class GymAdmin(LeafletGeoAdmin):
    list_display = ('name','description','image','geom','working_hours')



admin.site.register(Gym, GymAdmin)