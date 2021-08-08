from rest_framework import generics, serializers
from jobs.models import JobOffer
from jobs.api.serializers import JobOfferSerializer


class ListView(generics.ListCreateAPIView):
    querset = JobOffer.objects.all().order_by('-id')
    serializer_class = JobOfferSerializer

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    querset = JobOffer.objects.all()
    serializer_class = JobOfferSerializer
