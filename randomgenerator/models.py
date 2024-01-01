from django.conf import settings
from django.db import models


class RanGenModel(models.Model):
    name = models.CharField(max_length=100)
    game_id = models.CharField(max_length=5)
    my_list = models.TextField(null=True, blank=True)
    stake = models.IntegerField(null=True)
    win = models.IntegerField(null=True)

    def __str__(self):
        return self.name + ' ' + self.game_id + ' ' + self.my_list + ' ' + str(self.win)


class RanNums(models.Model):
    game_id = models.CharField(max_length=5)
    my_list = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.game_id + ' ' + self.my_list
