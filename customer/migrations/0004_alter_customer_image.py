# Generated by Django 5.0.1 on 2024-03-27 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_customer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(null=True, upload_to='customer'),
        ),
    ]
