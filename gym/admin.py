from django.contrib import admin
from .models import User,Gymnast,Trainer,GymManager,Chatroom,Post,Gym,Event,Join,Entry
# Register your models here.
admin.site.register(User)
admin.site.register(Gymnast)
admin.site.register(Trainer)
admin.site.register(GymManager)
admin.site.register(Chatroom)
admin.site.register(Post)
admin.site.register(Gym)
admin.site.register(Event)
admin.site.register(Join)
admin.site.register(Entry)
from leaflet.admin import LeafletGeoAdmin
from django.contrib.gis.admin import GeoModelAdmin
from .models import Gym



