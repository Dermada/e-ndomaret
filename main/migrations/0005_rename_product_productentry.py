# Generated by Django 5.1 on 2024-10-01 23:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_product_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='ProductEntry',
        ),
    ]