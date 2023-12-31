# Generated by Django 4.1.7 on 2023-09-23 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_cloth_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloth',
            name='color',
            field=models.CharField(choices=[('Черный', 'Черный'), ('Белый', 'Белый'), ('Синий', 'Синий'), ('Коричневый', 'Коричневый'), ('Зеленый', 'Зеленый'), ('Красный', 'Красный'), ('Желтый', 'Желтый'), ('Розвый', 'Розвый'), ('Фиолетовый', 'Фиолетовый'), ('Оранжевый', 'Оранжевый')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cloth',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
