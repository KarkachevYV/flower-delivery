# orders/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem, Flower
from .forms import OrderForm  # Импортируем форму для оформления заказа
from .serializers import OrderSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from catalog.models import Flower


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == 'client':
            return Order.objects.filter(customer=self.request.user)
        return super().get_queryset()


@login_required
def order_history(request):
    orders = Order.objects.filter(customer=request.user)
    return render(request, 'orders/orders_history.html', {'orders': orders})


@login_required
def cart(request):
    cart = request.session.get('cart', {})
    flower_ids = list(map(int, cart.keys()))  # Преобразование ключей в int
    flowers = Flower.objects.filter(id__in=flower_ids)
    return render(request, 'orders/cart.html', {'flowers': flowers})


def add_to_cart(request, flower_id):
    cart = request.session.get('cart', {})
    cart[flower_id] = cart.get(flower_id, 0) + 1
    request.session['cart'] = cart
    return redirect('catalog:flower_catalog')


@login_required
def checkout(request):
    initial_data = {
        'status': 'В ожидании',  # Начальный статус заказа, можно изменить при необходимости
    }

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.address = f"{request.user.country}, {request.user.region}, {request.user.city}, {request.user.street}, {request.user.house_number}"
            order.phone = request.user.phone_number
            order.save()

            for flower_id, quantity in request.session.get('cart', {}).items():
                flower = Flower.objects.get(id=flower_id)
                OrderItem.objects.create(order=order, flower=flower, quantity=quantity)

            request.session['cart'] = {}
            return redirect('accounts:profile')
    else:
        form = OrderForm(initial=initial_data)

    return render(request, 'orders/checkout.html', {'form': form})