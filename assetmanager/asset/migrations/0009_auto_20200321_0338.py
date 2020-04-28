# Generated by Django 2.2.1 on 2020-03-21 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0008_auto_20200315_0312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appreciate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('appreciation_rate', models.PositiveIntegerField(null=True)),
                ('appreciation_value', models.PositiveIntegerField(null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='Depreciate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('depreciation_rate', models.PositiveIntegerField(null=True)),
                ('depreciation_value', models.PositiveIntegerField(null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.Asset')),
            ],
        ),
        migrations.DeleteModel(
            name='Cumulative',
        ),
    ]