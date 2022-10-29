from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre = 'action')
    serializer_class = MovieSerializer

class FantasyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre = 'fantasy')
    serializer_class = MovieSerializer

class SciFiViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre = 'science fiction')
    serializer_class = MovieSerializer

class CrimeViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre = 'crime')
    serializer_class = MovieSerializer


#add science fiction, and crime