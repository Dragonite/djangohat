# Generated by Django 2.2.2 on 2019-11-09 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='site_key',
            field=models.CharField(blank=True, default='e1c3b40d863f410287a1c882afb11303', max_length=32, unique=True),
        ),
    ]