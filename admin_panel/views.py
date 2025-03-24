# admin_panel/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from accounts.models import CustomUser
from orders.models import Order
from catalog.models import Flower, Category
from .forms import UserManagementForm, OrderManagementForm, FlowerManagementForm

def is_admin(user):
    return user.is_authenticated and user.role == 'admin'

@user_passes_test(is_admin)
def dashboard(request):
    user_count = CustomUser.objects.count()
    product_count = Flower.objects.count()
    order_count = Order.objects.count()
    return render(request, 'admin_panel/dashboard.html', {
        'user_count': user_count,
        'product_count': product_count,
        'order_count': order_count,
    })

@user_passes_test(is_admin)
def manage_users(request):
    users = CustomUser.objects.all()

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = get_object_or_404(CustomUser, id=user_id)
        form = UserManagementForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('manage_users')
    else:
        form = UserManagementForm()

    return render(request, 'admin_panel/manage_users.html', {
        'users': users,
        'form': form
    })

@user_passes_test(is_admin)
def manage_orders(request):
    orders = Order.objects.all()

    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = get_object_or_404(Order, id=order_id)
        form = OrderManagementForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('manage_orders')
    else:
        form = OrderManagementForm()

    return render(request, 'admin_panel/manage_orders.html', {
        'orders': orders,
        'form': form
    })

@user_passes_test(is_admin)
def manage_products(request):
    flowers = Flower.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        flower_id = request.POST.get('flower_id')
        flower = get_object_or_404(Flower, id=flower_id)
        form = FlowerManagementForm(request.POST, instance=flower)
        if form.is_valid():
            form.save()
            return redirect('manage_products')
    else:
        form = FlowerManagementForm()

    return render(request, 'admin_panel/manage_products.html', {
        'flowers': flowers,
        'categories': categories,
        'form': form
    })
