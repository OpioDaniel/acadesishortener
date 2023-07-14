from django.db import models
from ..main.models import AcadeURL


class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, AcadeURL):
            obj, created = self.get_or_create(acade_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    acade_url = models.OneToOneField(AcadeURL, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)

# Create your models here.
