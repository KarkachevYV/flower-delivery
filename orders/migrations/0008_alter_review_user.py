# Generated by Django 5.1.7 on 2025-04-09 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_api', '0004_alter_botuser_user'),
        ('orders', '0007_alter_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot_api.botuser'),
        ),
    ]
