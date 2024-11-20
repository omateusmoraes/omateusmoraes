# Generated by Django 3.1.4 on 2024-07-06 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0009_auto_20240705_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('quantidade', models.IntegerField()),
                ('unidade', models.CharField(max_length=50)),
                ('valor_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
