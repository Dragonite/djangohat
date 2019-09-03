from django.db import models


class Users(models.Model):
    discord_id = models.CharField(primary_key=True, max_length=255)
    full_name = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    htb = models.CharField(max_length=255, blank=True, null=True)
    discord_tag = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'