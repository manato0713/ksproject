from django.contrib import admin

# Register your models here.
from .models import CustomUser,Buki,Category,Category2,Category3

class CustomUserAdmin(admin.ModelAdmin):

    list_display = ('id','username','first_name','last_name',)

    list_display_links = ('id','username',)


class BukiAdmin(admin.ModelAdmin):
    list_display = ('id','title','user',)

    list_display_links = ('id','title','user',)


class CategoryAdmin(admin.ModelAdmin):

     list_display = ('id','title',)

     list_display_links = ('id','title',)
     

class CategoryAdmin2(admin.ModelAdmin):

     list_display = ('id','title',)

     list_display_links = ('id','title',)

class CategoryAdmin3(admin.ModelAdmin):

     list_display = ('id','title',)

     list_display_links = ('id','title',)







admin.site.register(Category,CategoryAdmin)  
admin.site.register(Category2,CategoryAdmin2)  
admin.site.register(Category3,CategoryAdmin3)

admin.site.register(Buki,BukiAdmin)
admin.site.register(CustomUser,CustomUserAdmin)
