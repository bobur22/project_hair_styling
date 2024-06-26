# Generated by Django 4.2.6 on 2023-11-25 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beaty_salon', '0005_secpi1_model_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_num', models.CharField(max_length=13)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
            },
        ),
    ]
