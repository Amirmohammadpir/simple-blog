from django.db import models
from django.utils import timezone

class Article(models.Model):
  STATUS_CHOICE = [
    ("p" , "published"),
    ('d' , 'draft'),
  ]
  title = models.CharField(max_length=200)
  slug = models.SlugField(unique=True)
  content = models.TextField()
  published = models.DateTimeField()
  thumbnail = models.ImageField(upload_to='images/',default='default.jpg')
  created = models.DateTimeField(auto_now_add = True)
  updated = models.DateTimeField(auto_now=True)
  status = models.CharField(max_length=1, choices=STATUS_CHOICE)
  def __str__(self):
    return self.title[:15]
