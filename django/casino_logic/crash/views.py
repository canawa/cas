from django.shortcuts import render, HttpResponse
import random

def crash (request):
     return render(request,'crash/index.html')

def boss_fight(request):
     return HttpResponse('Тут будет босфайт')
def mines(request):
     return HttpResponse('Тут будут минки')
def roullete(request):
     return HttpResponse('Тут будет рулетка')
def ballon(request):
     return HttpResponse('Тут будет Ballon')

def plinko(request):
     return HttpResponse('1')
