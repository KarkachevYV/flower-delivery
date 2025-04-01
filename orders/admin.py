#orders/admin.py
from django.http import FileResponse
import os
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse, path
from django.utils.timezone import now
from django.shortcuts import render
from .models import Order, OrderItem
# from .views import download_pdf_report, download_excel_report

# admin.site.register(Order)
admin.site.register(OrderItem)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'created_at', 'report_links']
    list_filter = ['status', 'created_at']

    def get_urls(self):
        """Добавляем ссылки на отчёты в админке Django."""
        urls = super().get_urls()
        custom_urls = [
            path('download_pdf/', self.admin_site.admin_view(download_pdf_report), name='download_pdf_report'),
            path('download_excel/', self.admin_site.admin_view(download_excel_report), name='download_excel_report'),
        ]
        return custom_urls + urls

    def report_links(self, obj=None):
        """Добавляем кнопки в список заказов."""
        pdf_url = reverse("admin_panel:download_pdf_report")
        excel_url = reverse("admin_panel:download_excel_report")
        return mark_safe(
            f'<a href="{pdf_url}" class="button" style="margin-right: 10px;">📄 Скачать PDF</a>'
            f'<a href="{excel_url}" class="button">📊 Скачать Excel</a>'
        )


    report_links.short_description = "Скачать отчёты"

    def changelist_view(self, request, extra_context=None):
        """Добавляем кнопки скачивания в админку Django."""
        extra_context = extra_context or {}
        extra_context["report_links"] = self.report_links(None)
        return super().changelist_view(request, extra_context=extra_context)
    

def download_pdf_report(request):
    file_path = os.path.join('reports', f"daily_report_{now().date()}.pdf")
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    else:
        return FileResponse(open('reports/empty.pdf', 'rb'), content_type='application/pdf')

def download_excel_report(request):
    file_path = os.path.join('reports', f"daily_report_{now().date()}.xlsx")
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    else:
        return FileResponse(open('reports/empty.xlsx', 'rb'), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')