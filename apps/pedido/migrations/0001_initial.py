# Generated by Django 4.2.6 on 2023-10-24 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('LoginUser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pedido', models.DateTimeField(auto_now_add=True)),
                ('cliente_nome', models.CharField(max_length=100)),
                ('endereco_entrega', models.CharField(max_length=200)),
                ('produtos', models.ManyToManyField(to='LoginUser.produto')),
            ],
        ),
    ]
