from django.urls import path
from . import views


app_name = 'splapp'

urlpatterns = [
    path('',views.IndexView.as_view(), name = 'index'),

    path('buki',views.BukiView.as_view(), name = 'buki'),

    path('syuta',views.SyutaView.as_view(), name = 'syuta'),

    path('rora',views.RoraView.as_view(), name = 'rora'),

    path('tya',views.TyazyaView.as_view(), name = 'tya'),

    path('suro',views.SuroView.as_view(), name = 'suro'),

    path('bura',views.BurasuView.as_view(), name = 'bura'),

    path('hude',views.HudeView.as_view(), name = 'hude'),

    path('supin',views.SupinView.as_view(), name = 'supin'),

    path('manyu',views.ManyuView.as_view(), name = 'manyu'),

    path('syeru',views.SyeruView.as_view(), name = 'syeru'),

    path('waipa',views.WaipaView.as_view(), name = 'waipa'),

    path('sutori',views.SutoriView.as_view(), name = 'sutori'),


    path('main/<int:pk>/',views.MainView.as_view(),name ='main'),

    path(
        #マッチングさせるURL
        'contact/',

        #views.pyの中の使うクラス名
        views.ContactView.as_view(),

        name='contact'
    ),
]

