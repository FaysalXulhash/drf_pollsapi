from django.urls import path, include
from .views import (
    #PollApi,
    #PollDetailApi,
    ChoiceApi,
    VoteApi,
    PollViewSet,
)
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')


urlpatterns = [
    path('', include(router.urls)),
    #path('polls/', PollApi.as_view(), name='poll_api'),
    #path('polls/<int:pk>/', PollDetailApi.as_view(), name='poll_detail_api'),

    path('polls/<int:pk>/choices/', ChoiceApi.as_view(), name='choice_api'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', VoteApi.as_view(), name='vote_api'),

]
