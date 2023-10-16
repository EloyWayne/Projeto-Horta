# Generated by Django 4.2.6 on 2023-10-11 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginUser', '0004_produto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produto',
            options={'verbose_name': 'Produto', 'verbose_name_plural': 'Produto'},
        ),
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.CharField(choices=[('GR', 'Grão'), ('VE', 'Verdura'), ('FR', 'Fruta')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
