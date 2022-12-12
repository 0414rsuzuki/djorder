# Generated by Django 3.0.4 on 2022-09-22 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=30, null=True)),
                ('order_item', models.CharField(max_length=30, null=True)),
                ('order_count', models.IntegerField(null=True)),
                ('order_number', models.IntegerField(null=True)),
                ('order_date', models.DateTimeField(null=True)),
                ('order_manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_manager', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mail_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.EmailField(max_length=254, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Mail_company', to='order.Order_data')),
            ],
        ),
    ]