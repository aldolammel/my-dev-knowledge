from django.db import models


class EventAttack(models.Model):
    start_datetime = models.DateTimeField(
        ...
    )
    was_during_sleep = models.BooleanField(
       ...
    )
    duration = models.DurationField(
       ...
    )
    attack_type = models.ForeignKey(
       ...
    )
    intensity = models.ForeignKey(
       ...
    )
    affected_areas = models.ManyToManyField(
        ...
    )
    medicines = models.ManyToManyField(
        ...
    )
    place = models.ForeignKey(
        ...
    )