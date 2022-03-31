from rest_framework import serializers
from .models import Food

class FoodSerializer(serializers.ModelSerializer):
    #created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Food
        fields = ['name','cost','star','category'] 



class FoodDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Food
        fields = '__all__'