from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # 바로 User Model을 작성하지 않더라도,
    # 이후 유저 모델 커스텀을 위해서 미리 작성
    
    pass