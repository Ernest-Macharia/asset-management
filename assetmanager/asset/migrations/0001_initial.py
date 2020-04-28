# Generated by Django 2.2.1 on 2020-02-27 13:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('serial_number', models.PositiveIntegerField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=19)),
                ('acquisition_date', models.DateField(default=django.utils.timezone.now)),
                ('departments', models.CharField(choices=[('SELECT', 'SELECT'), ('finance', 'finance'), ('human resource', 'human resource'), ('procurement', 'procurement'), ('IT', 'IT'), ('marketing', 'marketing'), ('production', 'production')], default='SELECT', max_length=64)),
                ('category', models.CharField(choices=[('SELECT', 'SELECT'), ('machinery', 'machinery'), ('motor vehicle', 'motor vehicle'), ('computers', 'computers'), ('building', 'building'), ('lands', 'lands')], default='SELECT', max_length=64)),
                ('appreciation_rate', models.PositiveIntegerField()),
                ('appreciation_value', models.PositiveIntegerField()),
                ('depreciation_rate', models.PositiveIntegerField()),
                ('depreciation_value', models.PositiveIntegerField()),
            ],
        ),
    ]