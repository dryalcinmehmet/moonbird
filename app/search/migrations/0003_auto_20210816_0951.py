# Generated by Django 3.0.1 on 2021-08-16 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20210816_0232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('color', models.CharField(max_length=30, verbose_name='color')),
                ('description', models.TextField(verbose_name='description')),
                ('type', models.IntegerField(choices=[(1, 'Sedan'), (2, 'Truck'), (3, 'SUV')], verbose_name='type')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('country_code', models.CharField(max_length=2, verbose_name='country code')),
                ('created', models.DateField(verbose_name='created')),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='car',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Manufacturer', verbose_name='manufacturer'),
        ),
    ]