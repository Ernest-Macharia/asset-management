# Generated by Django 2.2.1 on 2020-03-14 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0004_auto_20200315_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='acquisition_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
