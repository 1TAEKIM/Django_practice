from django.db import models


# Create your models here.
class Movie(models.Model):
    
    # 각 변수값은 필드명
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    is_open = models.BooleanField()
    
    created_at = models.DateField(auto_now_add=True)
    
    
    