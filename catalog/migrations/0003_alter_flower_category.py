# Generated by Django 5.1.7 on 2025-03-27 06:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_flower_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.category'),
        ),
    ]
