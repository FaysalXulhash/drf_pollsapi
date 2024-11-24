from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.generics import (CreateAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView
                                     )
from rest_framework.response import Response
from .models import Poll, Vote, Choice
from .serializers import PollSerializer, VoteSerializer, ChoiceSerializer
# Create your views here.


# class PollApi(ListCreateAPIView):
#     queryset = Poll.objects.all()
#     serializer_class = PollSerializer
#
# class PollDetailApi(RetrieveUpdateDestroyAPIView):
#     queryset = Poll.objects.all()
#     serializer_class = PollSerializer

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
class ChoiceApi(ListCreateAPIView):
    #queryset = Choice.objects.all()

    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id = self.kwargs["pk"])
        return queryset
    serializer_class = ChoiceSerializer

class VoteApi(CreateAPIView):
    #queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def post(self, request, pk, choice_pk, format=None):
        voted_by = request.data.get("voted_by")
        data = {'choice': choice_pk, 'poll': pk, 'voted_by': voted_by}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




