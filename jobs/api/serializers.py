from rest_framework import serializers
from jobs.models import JobOffer

class JobOfferSerializer(serializers.ModelSerializer):
    class Meta:
        momdel = JobOffer
        fields = '__all__'