from django.urls import path, include
from .views import (
    PollApi,
    PollDetailApi,
    ChoiceApi,
    VoteApi,
)

urlpatterns = [
    path('poll-api/', PollApi.as_view(), name='poll_api'),
    path('choice-api/', ChoiceApi.as_view(), name='choice_api'),
    path('vote-api/', VoteApi.as_view(), name='vote_api'),
    path('poll-api/<int:pk>/', PollDetailApi.as_view(), name='poll_detail_api'),
]
