# Generated by Django 4.1.7 on 2023-08-21 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_cloth_size2_alter_cloth_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloth',
            name='gender',
            field=models.CharField(choices=[('Man', 'Man'), ('Woman', 'Woman'), ('Unisex', 'Unisex')], max_length=255, null=True),
        ),
    ]
