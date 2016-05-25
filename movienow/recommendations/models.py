from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Recommendation(models.Model):
    movie_id = models.CharField(max_length=255)
    rating = models.IntegerField()
    created_by = models.ForeignKey(User, related_name='recommends', editable=False)

    def __str__(self):
        return '{} rated {} by {}'.format(self.movie_id, self.rating, self.created_by)
