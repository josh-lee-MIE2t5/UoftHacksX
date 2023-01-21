from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
       class Meta:
            model = Event
            fields = ("_id", "title", "description", "location",
                    "_type", "startDate", "endDate", "registerationReq", "frequency")

