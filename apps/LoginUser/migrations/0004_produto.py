# Generated by Django 4.2.6 on 2023-10-11 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginUser', '0003_alter_produtor_options_alter_tipo_produtor_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
