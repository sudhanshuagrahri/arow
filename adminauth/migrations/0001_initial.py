# Generated by Django 3.1.6 on 2021-04-29 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Designers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('product_code', models.CharField(max_length=10)),
                ('nop', models.IntegerField(default=0)),
                ('uplpics', models.BooleanField(default=True)),
                ('desc', models.TextField(blank=True)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(default='uremail@gmail.com', max_length=254)),
                ('role', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturers',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Qty', models.IntegerField(default=0)),
                ('TimeFrame', models.DateTimeField(auto_now=True)),
                ('Courier_number', models.IntegerField(default=0)),
                ('Dated', models.DateField(auto_now=True)),
                ('comments', models.TextField(blank=True)),
                ('customer_details', models.ManyToManyField(to='adminauth.Designers')),
            ],
        ),
    ]
