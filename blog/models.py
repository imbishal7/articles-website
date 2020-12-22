from django.db import models
from django.utils import timezone
from django.urls import reverse
from tinymce.models import HTMLField
# Create your models here


class Post(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=70)
    published_date = models.DateTimeField(default=timezone.now)
    content = HTMLField()



    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})
    def __str__(self):
        return self.title
