# 📦 Проект «Доставка цветов»

## 📄 Описание проекта
Проект представляет собой веб-приложение и телеграм-бота для заказа цветов. Веб-приложение реализовано на Django с использованием Django REST Framework (DRF), а телеграм-бот — на библиотеке aiogram. Проект позволяет пользователям просматривать каталог, оформлять заказы, оставлять отзывы и управлять своими заказами. Администраторы могут просматривать аналитику заказов, изменять статусы и взаимодействовать с заказами через веб-интерфейс и телеграм-бот.

---

## 📁 Структура проекта
```
flower-delivery/
│── accounts/             # Приложение для управления пользователями
│   ├── __init__.py 
│   ├── migrations/
│   ├── admin.py
│   ├── decorators.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
│── admin_panel/          # Административная панель заказов
│   ├── __init__.py     
│   ├── urls.py
│   └── views.py
│
│── catalog/              # Приложение для каталога цветов
│   ├── __init__.py 
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
│── bot/                  # Телеграм-бот на aiogram
│   ├── __init__.py 
│   ├── handlers/          # Хендлеры команд и callback
│   │   ├── __init__.py
│   │   ├── commands.py
│   │   └── callbacks.py
│   ├── keyboards/         # Reply и Inline клавиатуры
│   │   ├── __init__.py
│   │   ├── reply.py
│   │   └── inline.py
│   ├── services/          # Логика взаимодействия с REST API
│   │   ├── __init__.py
│   │   └── api.py
│   ├── config.py          # Конфигурация токенов и настроек бота
│   └── main.py            # Запуск бота
│
│── flower_delivery/      # Основной проект Django
│   ├── __init__.py  
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
│── media/          # Медиафайлы (изображения букетов и профилей)
│── orders/         # Приложение для управления заказами
│   ├── __init__.py 
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
│── static/         # Статика (CSS, JS, изображения)
│   ├── css/
│   ├── js/
│   └── images/
│── templates/      # Шаблоны Django
│   ├── base.html
│   ├──  admin_panel/
│   │   ├──  dashboard.html
│   │   ├── manage_orders.html
│   │   ├── manage_products.html
│   │   └── manage_users.html
│   ├── accounts/
│   │   ├── admin_dashboard.html
│   │   ├── login.html
│   │   ├── logout.html
│   │   ├── register.html
│   │   └── profile.html
│   ├── catalog/
│   │   └── flower_catalog.html
│   └── orders/
│       ├── cart.html
│       ├── checkout.html
│       └── orders_history.html
│   
│── tests/
│── venv
│── .env
│── .gitignore
│── db.sqlite3
│── manage.py
│── README.md
└── requirements.txt
```

---

## 🚀 Запуск проекта
### 1. Клонирование репозитория:
```
git clone https://github.com/username/flower-delivery.git
cd flower-delivery
```

### 2. Создание виртуального окружения:
```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Установка зависимостей:
```
pip install -r requirements.txt
```

### 4. Настройка переменных окружения:
Создайте файл `.env` и добавьте переменные:
```
SECRET_KEY=ваш_секретный_ключ
DEBUG=True
ALLOWED_HOSTS=*
TELEGRAM_BOT_TOKEN=токен_вашего_бота
```

### 5. Миграции и создание суперпользователя:
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 6. Запуск проекта:
- Сервер Django:
```
python manage.py runserver
```
- Телеграм-бот:
```
python bot/main.py
```

---

## 📊 Функционал проекта
- Регистрация и аутентификация пользователей.
- Просмотр каталога цветов.
- Оформление заказа, повторное оформление и отмена заказа.
- Отправка уведомлений в Telegram при оформлении заказа.
- Административная панель для управления заказами и пользователями.
- Аналитика по заказам в Telegram и веб-интерфейсе.

---

## 🔧 Технологии и библиотеки
- Django, Django REST Framework
- aiogram — для телеграм-бота
- SQLite — база данных (на этапе разработки)
- Bootstrap — для оформления фронтенда
- JWT — аутентификация в REST API

---

## 🛠️ Планируемые доработки
- Поддержка PostgreSQL для продакшена.
- Расширение функционала аналитики.
- Улучшение взаимодействия бота и веб-приложения.

---

## 📩 Контакты
Если есть вопросы или предложения — обращайтесь!


