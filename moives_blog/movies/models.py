from django.db import models

# Create your models here.
class Movie(models.Model):
    # 각 변수값은 필드명
    title = models.CharField(max_length=20)
    content = models.TextField()