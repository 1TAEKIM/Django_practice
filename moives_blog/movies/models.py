from django.db import models
from django.utils import timezone

# Create your models here.
class Movie(models.Model):
    # 각 변수값은 필드명
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_open = models.BooleanField()
    
    created_at = models.DateField(auto_now_add=True)
    
    
    