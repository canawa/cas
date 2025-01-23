from django.db import models

# Create your models here.
class GameStats(models.Model):
    game_id =  models.IntegerField('Game_id', )
    coef = models.FloatField('Коэффициент')
    player_id = models.FloatField('ID игрока') 
    game_type = models.TextField('Тип игры')
    
    
    class Meta:
        verbose_name = 'Статистика Игр'
        verbose_name_plural = 'Статистика Игр'