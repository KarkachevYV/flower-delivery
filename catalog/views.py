#catalog/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Flower
from .serializers import FlowerSerializer
from django.shortcuts import render

# API ViewSet для работы с цветами
class FlowerViewSet(viewsets.ModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()

# Шаблон каталога для обычных пользователей
def flower_catalog(request):
    flowers = Flower.objects.filter(in_stock=True)
    return render(request, 'catalog/flower_catalog.html', {'flowers': flowers})

# def cart_views(request):
#     return render(request, 'catalog/cart.html') 