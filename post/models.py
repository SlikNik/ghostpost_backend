from django.db import models
from django.utils import timezone
import random

class GhostPost(models.Model):
    class BoastOrRoast(models.TextChoices):
        BOAST = 'B', ('Boast')
        ROAST = 'R', ('Roast')
    type_of_post  = models.CharField(
        max_length=2,
        choices=BoastOrRoast.choices,
        default=BoastOrRoast.BOAST,
    )
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    secret = models.CharField(max_length=7, null=True, blank=True)
    score = models.IntegerField(editable=False, default=0, null=True, blank=True)
    post_date = models.DateTimeField(default=timezone.now)
    last_update = models.DateTimeField(default=timezone.now)
   

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.score = self.up_votes - self.down_votes
        self.secret_key()
        super(GhostPost, self).save()

    def secret_key(self):
        keys = 'abcdefghijklmnopqrstuv0123456789'
        self.secret = ''.join(random.sample(keys, 6))
        return self.secret

        