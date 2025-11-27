from django.db import models

# Create your models here.

class UserComments(models.Model):
    title = models.CharField(
        verbose_name='ニックネーム',
        max_length=15
    )

    comment = models.TextField(
        verbose_name='コメント'
    )

    def __str__(self):


     return self.title