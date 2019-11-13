# Generated by Django 2.2.2 on 2019-11-13 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('discord_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('htb', models.CharField(blank=True, max_length=255, null=True)),
                ('discord_tag', models.CharField(blank=True, max_length=255, null=True)),
                ('site_verified', models.BooleanField(default=False)),
                ('site_key', models.CharField(blank=True, default='f26bab930a02483584607ad04b25694e', max_length=32, unique=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
