from django.db import models
# Create your models here.
from time import sleep

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    src = models.CharField('가입방법', max_length=20)
    created_on = models.DateTimeField('등록일자', auto_now_add=True)
    updated_on = models.DateTimeField('수정일자', auto_now=True)
    deleted_on = models.DateTimeField('삭제일자', blank=True, null=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class RollingPaperBoard(models.Model):
    title = models.CharField('보드이름', max_length=100)
    board_image = models.IntegerField('보드 그림 종류')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField('등록일자', auto_now_add=True)
    updated_on = models.DateTimeField('수정일자', auto_now=True)
    opened_at = models.DateTimeField('공개일자')
    link = models.CharField('공유 링크', max_length=30)

    class Meta:
        db_table = 'rolling_paper_board'

    def __str__(self):
        return f'{self.id}_{self.title}'

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    rolling_paper_board = models.ForeignKey(RollingPaperBoard, on_delete=models.CASCADE, related_name='rolling_paper_board_message_set')
    return_board = models.ForeignKey(RollingPaperBoard, null=True, on_delete=models.SET_NULL, related_name='return_board_message_set')
    contents = models.CharField(verbose_name='메시지 내용', max_length=500)
    acc_type = models.IntegerField(verbose_name='악세사리 타입')
    created_on = models.DateTimeField('등록일자', auto_now_add=True)
    updated_on = models.DateTimeField('수정일자', auto_now=True)

    class Meta:
        db_table = 'tree_message'
        verbose_name = '메시지'
        verbose_name_plural = '메시지 목록'

    def __str__(self):
        return f"[{self.created_on}]: {self.contents}"
