from django.urls import path, include
from . import views
urlpatterns = [
    path('crash/',views.crash),
    path('plinko/',views.plinko),
    path('boss_fight',views.boss_fight),
    path('ballon',views.ballon),
    path('roulette',views.roullete),
    path('mines',views.mines),
]