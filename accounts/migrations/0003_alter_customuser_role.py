# Generated by Django 5.1.7 on 2025-03-25 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Администратор'), ('moderator', 'Модератор'), ('user', 'Обычный пользователь'), ('guest', 'Гость')], default='user', max_length=30),
        ),
    ]
