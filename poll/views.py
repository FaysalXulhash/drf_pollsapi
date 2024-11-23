from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import (CreateAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView
                                     )
from rest_framework.response import Response
from .models import Poll, Vote, Choice
from .serializers import PollSerializer, VoteSerializer, ChoiceSerializer
# Create your views here.


class PollApi(ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class PollDetailApi(RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class ChoiceApi(ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class VoteApi(CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

