from django.db import models

htb_url_base = 'https://www.hackthebox.eu/profile/'

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

    def get_htb_url(self):
        if self.htb:
            return htb_url_base + str(self.htb)
        else:
            return None