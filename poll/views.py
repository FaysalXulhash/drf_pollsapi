from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.generics import (CreateAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView
                                     )
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Poll, Vote, Choice
from .serializers import PollSerializer, VoteSerializer, ChoiceSerializer
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
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

    def destroy(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk=self.kwargs["pk"])
        if not request.user == poll.created_by:
            raise PermissionDenied("You don't have permission to delete this poll!")
        return super().destroy(request, *args, **kwargs)
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsAuthenticated]

class ChoiceApi(ListCreateAPIView):
    # queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs["pk"])
        return queryset

    def post(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk=self.kwargs["pk"])
        if not request.user == poll.created_by:
            raise PermissionDenied("You don't have permission to create choice for this poll")
        return super().post(request, *args, **kwargs)


class VoteApi(CreateAPIView):
    # queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def post(self, request, pk, choice_pk, format=None):
        voted_by = request.data.get("voted_by")
        data = {'choice': choice_pk, 'poll': pk, 'voted_by': voted_by}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




