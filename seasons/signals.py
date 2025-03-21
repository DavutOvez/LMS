from django.db.models.signals import post_save ,pre_save
from django.dispatch import receiver
from seasons.models import Season

@receiver(post_save , sender = Season)
def make_seasons_inactive(sender , instance , created , **kwargs):
    if instance.status:
        Season.objects.all().exclude(id = instance.id).update(status = False)