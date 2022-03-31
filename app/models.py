from django.db import models
from django import forms

# Create your models here.
# 名前,所用金額,満足度,満腹度,必要時間,カテゴリー,詳細

class FoodCategory(models.TextChoices):
    HOME = 'HOME', '家'
    OUT = 'OUT', '外食'
    
class Food(models.Model):
    name = models.CharField('名前',max_length=50)
    cost = models.IntegerField('金額')
    star = models.IntegerField('満足度')
    satiety = models.IntegerField('満腹度')
    category = models.CharField(
        choices=FoodCategory.choices,
        verbose_name = 'カテゴリー',
        max_length= 50,
        # widget=forms.widgets.Select,
    )
    detail = models.TextField('詳細',   blank= True)

    created_at = models.DateTimeField('作成日',auto_now_add=True)

    def __str__(self):
        return self.name