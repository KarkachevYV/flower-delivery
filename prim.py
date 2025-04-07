```
│── bot/                  # Телеграм-бот на aiogram
│   ├── __init__.py 
│   ├── handlers/          # Хендлеры команд и callback
│   │   ├── __init__.py
│   │   ├── help.py
│   │   ├── link_profile.py
│   │   ├── orders.py
│   │   ├── profile.py
│   │   ├── reviews.py
│   │   └── start.py
│   ├── keyboards/         # Reply и Inline клавиатуры
│   │   ├── __init__.py
│   │   ├── reply.py
│   │   └── inline.py
│   ├── services/         
│   │   ├── __init__.py
│   │   └── analytics.py
│   ├── states/          
│   │   ├── __init__.py
│   │   └── review_states.py
│   ├── utils/          
│   │   ├── __init__.py
│   │   └── user_linking.py
│   ├── api.py 
│   ├── config.py          # Конфигурация токенов и настроек бота
│   ├── main.py   
│   ├── models.py  
│   ├── README.md 
│   └── requirements.txt            
```