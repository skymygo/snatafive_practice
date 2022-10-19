from django.db import models
# Create your models here.
from time import sleep

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    src = models.CharField("가입방법", max_length=20)
    share_link = models.CharField("공유 링크", max_length=100)
    created_on = models.DateTimeField("등록일자", auto_now_add=True)
    updated_on = models.DateTimeField("수정일자", auto_now=True)

