from django.shortcuts import render, HttpResponse
import secrets
import time
import json
from .models import GameStats
import asyncio
def crash_point():
          raw = secrets.randbelow(10**9) / 10**9
          if raw == 0:
               raw=0.001
          multiplier = 1 / raw * 0.95
          multiplier = round(multiplier, 2)
          if multiplier < 1:
               multiplier = secrets.randbelow(10**9) / 10**9
               multiplier = 1 / multiplier * 0.95
               multiplier = round(multiplier, 2)
               
               if multiplier<1:
                    multiplier=1.00
          
          return (multiplier) 


def crash (request):
     crash_game=crash_point()
     
     GameStats.objects.create(coef=crash_game)
     game_results = {
          'result': str(crash_game) + 'x'
          }
     
     with open("crash/static/crash/js/data.json", "w") as f:
          json.dump({"coefficient": crash_game}, f) 
          
    


     
     return render(request,'crash/index.html', game_results)

def move_to_main(request):
      return render(request, 'crash/index.html' )

def boss_fight(request):
     return render(request,'crash/boss_fight.html')
def mines(request):
     return render(request,'crash/mines.html')
def roullete(request):
     return render(request,'crash/roullete.html')
def ballon(request):
     return render(request,'crash/ballon.html')

def plinko(request):
     return render(request,'crash/plinko.html')

def stats(request):
    order = request.GET.get('order','game_id')
    data = GameStats.objects.order_by(order)
    context = {
         'direction' : 'asc' if not order.startswith('-') else 'desc'
    }
    return render(request, 'crash/all_game_stats.html', {'data':data })


