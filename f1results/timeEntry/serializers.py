from rest_framework import serializers 
from timeEntry.models import  timeEntry

class TimeEntrySerializer(serializers.ModelSerializer):
  class Meta:
    model = timeEntry
    fields = '__all__'


