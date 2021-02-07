from rest_framework.serializers import ModelSerializer
from .models import Survey, Option, Vote


class SurveySerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = "__all__"


class OptionSerializer(ModelSerializer):
    class Meta:
        model = Option
        fields = "__all__"


class VoteSerializer(ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"
