from django.urls import path

from . import views


app_name = 'quiz'

urlpatterns = [
    
    path(
        'quiz/',
        views.quizView.as_view(),
        name = 'quiz'
    ),

    path(
        'kaisetu',views.KaisetuView.as_view(),
        name = 'kaisetu'
    )

    
]