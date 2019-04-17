from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils import timezone


class GameDataModel(models.Model):

    unique_id = models.CharField(unique=True, max_length=1000)
    game_data = JSONField()
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField()

    def __str__(self):
        return '<GameDataModel %r>' % self.id

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(GameDataModel, self).save(*args, **kwargs)

