from django.shortcuts import render, HttpResponse
import random

def crash (request):
     return render(request,'crash/index.html')

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
