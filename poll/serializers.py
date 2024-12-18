from rest_framework import serializers
from .models import Poll, Choice, Vote


class VoteSerializer(serializers.ModelSerializer):
    #voted_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Vote
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)
    # choices = serializers.StringRelatedField(read_only = True)
    # created_by = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = Poll
        fields = '__all__'
