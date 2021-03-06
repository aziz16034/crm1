# Generated by Django 2.2.14 on 2020-10-01 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maintainance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('SOLD', 'Item already purchased'), ('AVAILABLE', 'Item ready to be purchased'), ('RESTOCKING', 'Item restocking in few days')], default='Sold', max_length=10)),
                ('description', models.CharField(default='try', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('SOLD', 'Item already purchased'), ('AVAILABLE', 'Item ready to be purchased'), ('RESTOCKING', 'Item restocking in few days')], default='Sold', max_length=10)),
                ('description', models.CharField(default='try', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('SOLD', 'Item already purchased'), ('AVAILABLE', 'Item ready to be purchased'), ('RESTOCKING', 'Item restocking in few days')], default='Sold', max_length=10)),
                ('description', models.CharField(default='try', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stiching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('SOLD', 'Item already purchased'), ('AVAILABLE', 'Item ready to be purchased'), ('RESTOCKING', 'Item restocking in few days')], default='Sold', max_length=10)),
                ('description', models.CharField(default='try', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Weaving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('SOLD', 'Item already purchased'), ('AVAILABLE', 'Item ready to be purchased'), ('RESTOCKING', 'Item restocking in few days')], default='Sold', max_length=10)),
                ('description', models.CharField(default='try', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
