# Generated by Django 2.2.1 on 2020-03-14 22:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_auto_20200315_0104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cumulative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('appreciation_rate', models.PositiveIntegerField(null=True)),
                ('appreciation_value', models.PositiveIntegerField(null=True)),
                ('depreciation_rate', models.PositiveIntegerField(null=True)),
                ('depreciation_value', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='asset',
            name='appreciation_rate',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='appreciation_value',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='depreciation_rate',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='depreciation_value',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='value',
        ),
        migrations.AlterField(
            model_name='asset',
            name='acquisition_date',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]