# Generated by Django 3.0.2 on 2020-02-01 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0001_initial'),
        ('manifests', '0005_auto_20200201_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manifestinfo',
            name='cargo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='cargos.Cargo', verbose_name='关联库存'),
        ),
    ]
