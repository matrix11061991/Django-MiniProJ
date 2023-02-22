from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 200)
	slug = models.SlugField(max_length = 200)
	body = models.TextField()
	created = models.DateTimeField(auto_now = True)
	uptaded = models.DateTimeField(auto_now = True)
	publish = models.DateTimeField(default = timezone.now())
	author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'posted')
