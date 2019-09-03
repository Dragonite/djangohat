from django.db import models

# Event Model

class Event(models.Model):
    title = models.CharField(max_length=100, default="Ethical Hacking Meeting - Weekly Meetup")
    location = models.CharField(max_length=100, default="G01 at CSSE")
    time = models.DateTimeField()
    info = models.TextField(default="Bring your laptops!")
