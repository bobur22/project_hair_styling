# Generated by Django 4.2.6 on 2023-11-24 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beaty_salon', '0004_categories_remove_secpi1_model_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='secpi1_model',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beaty_salon.categories'),
        ),
    ]