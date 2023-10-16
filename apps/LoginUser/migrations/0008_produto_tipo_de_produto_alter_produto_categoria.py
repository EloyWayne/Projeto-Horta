# Generated by Django 4.2.6 on 2023-10-11 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LoginUser', '0007_alter_produtor_options_produtor_tipo_de_produtor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='tipo_de_produto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='LoginUser.produtor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.CharField(max_length=100),
        ),
    ]
