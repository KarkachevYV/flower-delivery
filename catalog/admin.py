# catalog/admin.py
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Flower

class FlowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'get_image')  # Добавляем фото в список
    readonly_fields = ('get_image',)  # Делаем поле для просмотра фото
    fields = ('name', 'description', 'price', 'image', 'get_image')  # Отображаем фото в деталях

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="80" height="80" />')
        return "Нет фото"

    get_image.short_description = "Фото"

admin.site.register(Flower, FlowerAdmin)
