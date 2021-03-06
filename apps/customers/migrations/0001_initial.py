# Generated by Django 3.0.2 on 2020-02-01 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='客户姓名')),
                ('mobile_phone', models.CharField(max_length=20, verbose_name='客户电话')),
            ],
            options={
                'verbose_name': '客户信息',
                'verbose_name_plural': '客户信息',
            },
        ),
        migrations.CreateModel(
            name='CustomerLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labelname', models.TextField(verbose_name='商标名称')),
                ('image', models.BinaryField(verbose_name='照片')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customers.Customer', verbose_name='客户')),
            ],
            options={
                'verbose_name': '客户商标',
                'verbose_name_plural': '客户商标',
            },
        ),
        migrations.AddConstraint(
            model_name='customerlabel',
            constraint=models.UniqueConstraint(fields=('customer', 'labelname'), name='unique_customerlabel'),
        ),
    ]
