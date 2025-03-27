# admin_panel/views.py
from django.db.models import Q
from datetime import datetime
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from accounts.models import CustomUser
from orders.models import Order, OrderItem
from catalog.models import Flower, Category
from .forms import UserManagementForm, OrderManagementForm, FlowerManagementForm, CategoryForm

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
            return redirect('admin_panel:manage_users')
    else:
        form = UserManagementForm()

    return render(request, 'admin_panel/manage_users.html', {
        'users': users,
        'form': form
    })


@user_passes_test(lambda u: u.is_authenticated and u.role == 'admin')
def manage_orders(request):
    orders_list = Order.objects.all().order_by('-created_at')  # Сортировка по дате создания (от новых к старым)
    
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        try:
            start_dt = datetime.strptime(start_date, "%Y-%m-%d")
            end_dt = datetime.strptime(end_date, "%Y-%m-%d")
            orders_list = orders_list.filter(created_at__date__range=[start_dt, end_dt])
        except ValueError:
            pass  # Если формат даты некорректен, фильтр не применяется
    
    paginator = Paginator(orders_list, 10)  # Показываем по 10 заказов на странице

    page_number = request.GET.get('page')
    orders = paginator.get_page(page_number)

    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = get_object_or_404(Order, id=order_id)
        form = OrderManagementForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('admin_panel:manage_orders')
    else:
        form = OrderManagementForm()

    return render(request, 'admin_panel/manage_orders.html', {
        'orders': orders,
        'form': form
    })

@staff_member_required
def manage_products(request):
    flowers = Flower.objects.all()
    categories = Category.objects.all()
    form = FlowerManagementForm()
    category_form = CategoryForm()
    editing = False  # Флаг для отслеживания режима редактирования
    selected_flower = None  # Для хранения текущего редактируемого товара

    if request.method == 'POST':
        if 'flower_id' in request.POST:  # Редактирование
            selected_flower = get_object_or_404(Flower, id=request.POST['flower_id'])
            form = FlowerManagementForm(request.POST, instance=selected_flower)
            editing = True
        else:  #  Добавление нового товара
            form = FlowerManagementForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('admin_panel:manage_products')

    # Если был GET-запрос с параметром `edit_id`, то заполняем форму товара
    elif 'edit_id' in request.GET:
        selected_flower = get_object_or_404(Flower, id=request.GET['edit_id'])
        form = FlowerManagementForm(instance=selected_flower)
        editing = True

    return render(request, 'admin_panel/manage_products.html', {
        'flowers': flowers,
        'categories': categories,
        'form': form,
        'category_form': category_form,
        'editing': editing,
        'selected_flower': selected_flower
    })

@staff_member_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel:manage_products')
    return redirect('admin_panel:manage_products')

def repeat_order(request, order_id):
    old_order = get_object_or_404(Order, id=order_id)
    new_order = Order.objects.create(user=old_order.user, status='new')

    for item in old_order.items.all():
        OrderItem.objects.create(
            order=new_order,
            flower=item.flower,
            quantity=item.quantity,
            price=item.price
        )

    return redirect('cart')  # Перенаправление в корзину
