# Generated by Django 4.2.13 on 2024-06-08 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_cargo_created_at_cargo_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='robo',
            name='nome_robo',
            field=models.CharField(default='Nome Padrão', max_length=255),
        ),
    ]
