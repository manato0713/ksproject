from django.contrib import admin

from .models import Quiz


class QuizAdmin(admin.ModelAdmin):
    list_display = ('id','title','user')

    list_display_links = ('id','title',)

admin.site.register(Quiz,QuizAdmin)  

# Register your models here.
