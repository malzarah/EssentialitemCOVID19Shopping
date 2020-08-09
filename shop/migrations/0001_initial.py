# Generated by Django 3.0.4 on 2020-08-09 07:08

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
            name='item',
            fields=[
                ('item_ID', models.AutoField(primary_key=True, serialize=False)),
                ('itemName', models.CharField(default='none', max_length=100)),
                ('itemDescription', models.CharField(default='', max_length=200)),
                ('itemEssentialFlag', models.BooleanField(default='True')),
                ('itemQty', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='usage',
            fields=[
                ('usage_ID', models.AutoField(primary_key=True, serialize=False)),
                ('usagePerc', models.FloatField(default=0.0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.item')),
            ],
        ),
        migrations.CreateModel(
            name='store',
            fields=[
                ('store_ID', models.AutoField(primary_key=True, serialize=False)),
                ('store_NAME', models.CharField(max_length=500)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.item')),
            ],
        ),
        migrations.CreateModel(
            name='archive',
            fields=[
                ('archive_ID', models.AutoField(primary_key=True, serialize=False)),
                ('itemName', models.CharField(max_length=200)),
                ('itemDescription', models.CharField(max_length=500)),
                ('itemEssentialFlag', models.BooleanField(default=True)),
                ('itemQty', models.IntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.item')),
            ],
        ),
    ]
