from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
"""
      User
    #ユーザのモデル
    username,password,is_authenticated
"""
class Card(models.Model):
    """"カードのモデル"""
    title = models.CharField(max_length=256)
    content = models.TextField()
    liked = models.IntegerField(default=0)
    card_date = models.DateTimeField('date published', default=timezone.now)
    card_tag = models.TextField()
    card_caregory = models.TextField()
    user = models.ForeignKey(User,related_name='cards',on_delete=models.CASCADE,default="0")

class Request(models.Model):
    """"リクエストのモデル"""
    title = models.CharField(max_length=256)
    content = models.TextField()
    request_tag = models.TextField()
    request_date = models.DateTimeField('date published', default=timezone.now)
    request_category = models.TextField()
    user = models.ForeignKey(User,related_name='requests',on_delete=models.CASCADE,default="0")

class ProgrammingLanguage(models.Model):
    """"プログラミング言語のモデル"""
    language_name = models.CharField(max_length=256)
    language_color = models.TextField()

class Tag(models.Model):
    name = models.CharField(max_length=256)

class Category(models.Model):
    name = models.CharField(max_length=256)