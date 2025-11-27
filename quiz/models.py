from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

from splapp.models import CustomUser









class Quiz(models.Model):


    
    
    user = models.ForeignKey(
        CustomUser,
        verbose_name='武器の名前',
        on_delete=models.CASCADE
    )

    title = models.CharField(
        verbose_name='射程',
        max_length=10
    )



    

    

    comment= models.TextField(
        verbose_name='空',
         blank=True,
        
      
    )

    comment2 =models.TextField(
        verbose_name='空',
        blank=True,
    )


    


    image1 = models.ImageField(
        verbose_name='武器の写真',
        upload_to='photos',
        null=True,
    )

    def __str__(self):


     return self.title


# Create your models here.
