# Generated by Django 3.2.25 on 2024-07-03 06:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngresoVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.CharField(max_length=50)),
                ('Cantidad', models.CharField(max_length=50)),
                ('Nombre_encargado', models.CharField(max_length=50)),
                ('Precio', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='ingresostock',
            name='Cantidad',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
