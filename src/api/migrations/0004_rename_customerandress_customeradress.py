# Generated by Django 5.1.7 on 2025-03-25 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_customer_complement_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomerAndress',
            new_name='CustomerAdress',
        ),
    ]
