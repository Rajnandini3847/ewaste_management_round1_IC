# Generated by Django 4.1.4 on 2022-12-28 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_bin_status_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bin_status',
            name='status',
            field=models.CharField(blank=True, choices=[('y', 'filled'), ('n', 'notfilled')], default='', max_length=60, verbose_name='status'),
        ),
    ]
