from django.contrib import admin

# Register your models here.
from .models import UserComments

class UC(admin.ModelAdmin):

 list_display = ('id','title','comment',)

    
 list_display_links = ('id','title','comment',)

admin.site.register(UserComments,UC)  
