# 📦 Проект «Доставка цветов»

# 🚀 Flower Delivery – интернет-магазин цветов

## 📄 Описание проекта
Проект представляет собой веб-приложение и телеграм-бота для заказа цветов. Веб-приложение реализовано на Django с использованием Django REST Framework (DRF), а телеграм-бот — на библиотеке aiogram. Проект позволяет пользователям регистрироваться на сайте, проходить аутентификацию на сайте и в боте, просматривать каталог, оформлять заказы, делать повторный заказ на сайте, просматривать статус заказа и и информацию о заказе, как на сайте , так и в боте. Администраторы могут просматривать аналитику заказов, выводить её в файлы pdf и 
 в xlsx, управлять покупателями, товарами и заказами, в том числе изменять статусы заказов.

---

## 📁 Структура проекта
```
flower-delivery/
│── accounts/             # Приложение для управления пользователями
│── admin_panel/          # Административная панель заказов
│── catalog/              # Приложение для каталога цветов
│── bot/                  # Телеграм-бот на aiogram
│── flower_delivery/      # Основной проект Django
│── media/                # Медиафайлы (изображения букетов и профилей)
│── orders/               # Приложение для управления заказами
│   ├── management/  
│   │   └── commands/
│   │        └── generate_daily_report.py  # Скрипт для генерации отчёта
│   ├── templatetags/  
│   │   └── cart_filters.py
│   ├── tasks.py          # Фоновые задачи Celery
│   ├── views.py          # Обработчик export_daily_report(request)
│── static/               # Статика (CSS, JS, изображения)
│── templates/            # Шаблоны Django
│── tests/                # Тесты
│── venv/                 # Виртуальное окружение
│── .env                  # Конфигурация окружения
│── .gitignore
│── celery-schedule.bak
│── celery-schedule.dat
│── celery-schedule.dir
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

## 🛠 Фоновые задачи (Celery + Redis)
Проект использует Celery для фоновых задач, а Redis в качестве брокера сообщений.

### 1. Запуск Redis
Перед запуском Celery убедитесь, что Redis работает:
```
sudo systemctl status redis  # Проверка статуса
sudo systemctl start redis   # Запуск (если не работает)

```

### 2. Запуск Celery worker
```
celery -A flower_delivery worker --loglevel=info

```

### 3. Запуск Celery Beat
```
celery -A flower_delivery beat --loglevel=info

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

## 📊 Аналитика и статистика
Для сбора статистики используется Celery Beat, который по расписанию запускает генерацию отчётов.

 - Фоновая задача Celery (orders/tasks.py) обрабатывает заказы и формирует отчёт.

 - Команда Django (orders/management/commands/generate_daily_report.py) выполняется по расписанию.

 - Ручной экспорт отчёта (export_daily_report(request)) доступен через Django Views.


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


