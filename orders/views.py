# orders/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem, Flower
from .forms import OrderForm  # Импортируем форму для оформления заказа
from .serializers import OrderSerializer
from django.shortcuts import render, redirect, get_object_or_404
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
def repeat_order(request, order_id):
    old_order = get_object_or_404(Order, id=order_id, customer=request.user)

    new_order = Order.objects.create(customer=request.user, status='new')

    cart = request.session.get('cart', {})  # Загружаем текущую корзину

    for item in old_order.items.all():
        OrderItem.objects.create(
            order=new_order,
            flower=item.flower,
            quantity=item.quantity,
            price=item.flower.price  # Берём цену из модели Flower
        )
        cart[str(item.flower.id)] = cart.get(str(item.flower.id), 0) + item.quantity  # Кладём в корзину

    request.session['cart'] = cart  # Сохраняем в сессии
    request.session.modified = True  # Помечаем, что сессия изменилась

    return redirect('orders:cart')

@login_required
def order_history(request):
    orders = Order.objects.filter(customer=request.user)
    return render(request, 'orders/order_history.html', {'orders': orders})



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
                OrderItem.objects.create(
                    order=order,
                    flower=flower,
                    quantity=quantity,
                    price=flower.price  # ✅ Добавили цену
                )
            request.session['cart'] = {}   # Очищаем корзину после заказа
            return redirect('orders:order_history')
    else:
        form = OrderForm(initial=initial_data)

    return render(request, 'orders/checkout.html', {'form': form})