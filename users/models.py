from django.db import models
from django.contrib.auth.models import User
import uuid

htb_url_base = 'https://www.hackthebox.eu/badge/image/'

class Users(models.Model):

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    discord_id = models.CharField(primary_key=True, max_length=255)
    full_name = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    htb = models.CharField(max_length=255, blank=True, null=True)
    discord_tag = models.CharField(max_length=255, blank=True, null=True)
    discord_avatar = models.CharField(max_length=255, blank=True, null=True)
    site_verified = models.BooleanField(default=False)
    site_key = models.CharField(max_length=32, blank=True, unique=True, default=uuid.uuid4().hex)

    def __str__(self):
        return self.discord_tag

    def get_htb_url(self):
        if self.htb:
            return htb_url_base + str(self.htb)
        else:
            return None