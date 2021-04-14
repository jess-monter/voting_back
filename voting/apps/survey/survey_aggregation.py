from dataclasses import dataclass
from django.db.models import Count
from .models import Vote


@dataclass
class SurveyAggregation:
    survey: object

    def get_result(self):
        result_set = (
            Vote.objects.values("option__id", "option__content")
            .annotate(total=Count("id"))
            .filter(option__survey=self.survey)
            .order_by("total")
        )
        result_set = list(result_set)
        first = result_set[1:][0]
        last = result_set[:-1][0]
        result = {"votes": result_set, "overview": {"first": first, "last": last}}
        return result
