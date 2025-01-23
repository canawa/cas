from django.shortcuts import render, HttpResponse
import secrets
import time
   

def crash_point():
          multiplier = secrets.randbelow(10**9) / 10**9
          multiplier = 1 / multiplier * 0.95
          multiplier = round(multiplier, 2)
          if multiplier < 1:
               multiplier = secrets.randbelow(10**9) / 10**9
               multiplier = 1 / multiplier * 0.8
               multiplier = round(multiplier, 2)
               if multiplier<1:
                    multiplier=1.00
          
          return str(multiplier) + 'x'
               

def crash (request):
    
     game_results = {
          'result': crash_point()
     }
     
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
    return render(request, 'crash/all_game_stats.html')
