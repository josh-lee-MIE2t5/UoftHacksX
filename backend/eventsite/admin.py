from django.contrib import admin
from .models import Event

# Register your models here.


class EventSiteAdmin(admin.ModelAdmin):
    list_display = ("_id", "title", "description", "location",
                    "_type", "startDate", "endDate", "registerationReq", "frequency")


admin.site.register(Event, EventSiteAdmin)
