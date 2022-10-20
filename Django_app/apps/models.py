from django.db import models
# Create your models here.
from time import sleep

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    src = models.CharField('가입방법', max_length=20)
    share_link = models.CharField('공유 링크', max_length=100)
    created_on = models.DateTimeField('등록일자', auto_now_add=True)
    updated_on = models.DateTimeField('수정일자', auto_now=True)
    deleted_on = models.DateTimeField('삭제일자', blank=True, null=True)

    class Meta:
        db_table = 'user'

class Message(models.Model):
    type = models.CharField(max_length=20)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_message_set')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver_message_set')
    is_confirmed = models.BooleanField(verbose_name='리뷰 확인 여부', default=False)
    acc_type = models.IntegerField(verbose_name='악세사리 타입')

    class Meta:
        db_table = 'tree_message'
        verbose_name = '메시지'
        verbose_name_plural = '메시지 목록'