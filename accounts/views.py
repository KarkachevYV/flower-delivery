# accounts/views.py

from django.shortcuts import render, redirect
from accounts.decorators import role_required
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from accounts.models import CustomUser
from orders.models import Order
from django.db.models import Sum
from django.db.utils import IntegrityError
import logging

logger = logging.getLogger(__name__)

@role_required(['admin'])
def admin_dashboard(request):
    user_count = CustomUser.objects.count()
    order_count = Order.objects.count()
    total_revenue = Order.objects.aggregate(Sum('total_amount'))['total_amount__sum'] or 0

    context = {
        'user_count': user_count,
        'order_count': order_count,
        'total_revenue': total_revenue,
    }
    return render(request, 'accounts/admin_dashboard.html', context)

def home(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('accounts:profile')
            except IntegrityError:
                form.add_error(None, "Пользователь с таким именем или номером телефона уже существует.")
        else:
            print("Форма не валидна:", form.errors)
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

def logout(request):
    auth_logout(request)
    return redirect('base')
