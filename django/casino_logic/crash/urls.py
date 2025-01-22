from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.crash, name='crash'),
    path('plinko/',views.plinko, name='plinko'),
    path('boss_fight',views.boss_fight, name='boss_fight'),
    path('ballon',views.ballon,name='ballon'),
    path('roulette',views.roullete,name='roulette'),
    path('mines',views.mines,name='mines'),
]