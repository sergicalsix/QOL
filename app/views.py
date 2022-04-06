from django.shortcuts import render
from django.views.generic import View
from rest_framework import generics
from .serializers import FoodSerializer, FoodDetailSerializer
from .models import Food
from django_filters import rest_framework as filters
# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/index.html')

class FoodFilter(filters.FilterSet):
    # filterの変数がクエリとなる
    name__contains = filters.CharFilter(field_name='name', lookup_expr='contains')

    cost__lte = filters.NumberFilter(field_name='cost', lookup_expr='lte')
    cost__gte = filters.NumberFilter(field_name='cost', lookup_expr='gte')
    star__lte = filters.NumberFilter(field_name='star', lookup_expr='lte')
    star__gte = filters.NumberFilter(field_name='star', lookup_expr='gte')
    satiety__lte = filters.NumberFilter(field_name='satiety', lookup_expr='lte')
    satiety__gte = filters.NumberFilter(field_name='satiety', lookup_expr='gte')
    
    class Meta:
        model = Food
        fields = '__all__'
class FoodViews(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = FoodFilter

class FoodDetailViews(generics.RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodDetailSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = FoodFilter
