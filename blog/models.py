from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

today = timezone.now
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(default=today)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    def total_likes(self):
        return self.like.count()
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})