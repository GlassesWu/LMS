# Generated by Django 3.0.2 on 2020-02-01 16:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('storages', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CargoBoxType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=4, verbose_name='包装类型ID')),
                ('typename', models.TextField(verbose_name='包装类型')),
            ],
            options={
                'verbose_name': '包装类型',
                'verbose_name_plural': '包装类型',
            },
        ),
        migrations.CreateModel(
            name='CargoType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=4, verbose_name='货物类型ID')),
                ('typename', models.TextField(blank=True, null=True, verbose_name='货物类型')),
            ],
            options={
                'verbose_name': '货物类型',
                'verbose_name_plural': '货物类型',
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='流水号')),
                ('quantity', models.IntegerField(verbose_name='货物数量')),
                ('is_split', models.BooleanField(default=False, verbose_name='是否拆分')),
                ('is_assign', models.BooleanField(default=False, verbose_name='是否分配货单')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='入库时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='storages.Storage', verbose_name='存放位置')),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cargos.CargoBoxType', verbose_name='包装类型')),
                ('customerlabel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customers.CustomerLabel', verbose_name='货物商标')),
                ('parent_uuid', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cargos.Cargo', verbose_name='归属流水号')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cargos.CargoType', verbose_name='货品类型')),
            ],
            options={
                'verbose_name': '货物信息',
                'verbose_name_plural': '货物信息',
            },
        ),
    ]
