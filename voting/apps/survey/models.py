from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Survey(models.Model):
    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Closed", "Closed"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "survey"
        verbose_name = "Survey"
        verbose_name_plural = "Surveys"

    def __str__(self):
        return self.title


class Option(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "option"
        verbose_name = "Option"
        verbose_name_plural = "Options"

    def __str__(self):
        return self.content


class Vote(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "vote"
        verbose_name = "Vote"
        verbose_name_plural = "Votes"

    def __str__(self):
        return f"{self.option.content}"
