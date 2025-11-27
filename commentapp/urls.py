from . import views

from django.urls import path


app_name = 'comment'

urlpatterns = [
    
    path(
        'comment/',
        views.CommentView.as_view(),
        name = 'comment'
    ),

    path(
        'comeiti/',
        views.ComeitiView.as_view(),
        name = 'comeiti'
    )
]