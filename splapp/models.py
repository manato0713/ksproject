from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser






class CustomUser(AbstractUser):

    pass

class Category(models.Model):
    title = models.CharField(
        verbose_name='武器の種類',
        max_length=20
    )
    def __str__(self):
        return self.title

class Category2(models.Model):
    title = models.CharField(
        verbose_name='サブの種類',
        max_length=20
    )
    def __str__(self):
        return self.title

class Category3(models.Model):
    title = models.CharField(
        verbose_name='スペシャルの種類',
        max_length=20
    )
    def __str__(self):
        return self.title


class Buki(models.Model):


    
    
    user = models.ForeignKey(
        CustomUser,
        verbose_name='武器の名前',
        on_delete=models.CASCADE
    )

    title = models.CharField(
        verbose_name='評価(1~5)',
        max_length=10

    )

    category = models.ForeignKey(
        Category,
        verbose_name='武器の種類',
        on_delete=models.PROTECT
    )

    category2 = models.ForeignKey(
        Category2,
        verbose_name='サブの種類',
        on_delete=models.PROTECT
    )

    category3 = models.ForeignKey(
        Category3,
        verbose_name='スペシャルの種類',
        on_delete=models.PROTECT
    )

    

    

    comment= models.TextField(
        verbose_name='武器の主な性能',
        
      
    )

    comment2 =models.TextField(
        verbose_name='作成者からのコメント',
        blank=True,
    )


    


    image1 = models.ImageField(
        verbose_name='武器の写真',
        upload_to='photos',
        null=True,
    )

    def __str__(self):


     return self.title
