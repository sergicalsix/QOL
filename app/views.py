from django.shortcuts import render
from django.views.generic import View
from rest_framework import generics
from .serializers import FoodSerializer
from .models import Food
# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/index.html')

class FoodViews(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodDetailViews(generics.RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer