from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import SurveyViewSet, OptionViewSet, VoteViewSet

router = DefaultRouter()
router.register(r"surveys", SurveyViewSet, basename="survey")
router.register(r"options", OptionViewSet, basename="option")
router.register(r"votes", VoteViewSet, basename="vote")

urlpatterns = [
    url(r"^", include(router.urls)),
]
