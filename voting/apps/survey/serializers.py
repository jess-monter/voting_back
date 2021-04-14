from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Survey, Option, Vote
from .survey_aggregation import SurveyAggregation


class SurveySerializer(ModelSerializer):

    results = SerializerMethodField(read_only=True)

    class Meta:
        model = Survey
        fields = "__all__"

    def get_results(self, obj):
        return SurveyAggregation(obj).get_result()


class OptionSerializer(ModelSerializer):
    class Meta:
        model = Option
        fields = "__all__"


class VoteSerializer(ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"
