from rest_framework.viewsets import ModelViewSet
from .models import Survey, Option, Vote
from .serializers import SurveySerializer, OptionSerializer, VoteSerializer


class SurveyViewSet(ModelViewSet):

    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class OptionViewSet(ModelViewSet):

    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class VoteViewSet(ModelViewSet):

    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
