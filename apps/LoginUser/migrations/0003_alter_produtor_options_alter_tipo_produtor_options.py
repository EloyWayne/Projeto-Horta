# Generated by Django 4.2.6 on 2023-10-11 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LoginUser', '0002_alter_endereço_options_alter_produtor_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produtor',
            options={'verbose_name': 'Produtor', 'verbose_name_plural': 'Produtor'},
        ),
        migrations.AlterModelOptions(
            name='tipo_produtor',
            options={'verbose_name': 'Tipo Produtor', 'verbose_name_plural': 'Tipo Produtor'},
        ),
    ]
