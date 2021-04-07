from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Vote
from .serializers import VoteSerializer

from asgiref.sync import async_to_sync
import channels.layers


@receiver(post_save, sender=Vote)
def send_notification(sender, instance, created, **kwargs):
    if created:
        notification = VoteSerializer(instance=instance).data
        layer = channels.layers.get_channel_layer()
        async_to_sync(layer.group_send)(
            "notification", {"type": "notification", "message": notification},
        )
