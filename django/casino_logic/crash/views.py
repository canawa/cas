from django.shortcuts import render, HttpResponse
import random

def crash (request):
     game_results = {
          'result': [2.56, 1.23, 45.2]
     }
     
     return render(request,'crash/index.html', game_results)

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
