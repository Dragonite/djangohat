from django.db import models
from django.utils import timezone

# Event Model

class Event(models.Model):

	DEFAULT_TITLE = "Ethical Hacking Meeting - Weekly Meetup"
	DEFAULT_LOCATION = "G01 at CSSE"
	DEFAULT_INFO = "Bring your laptops"

	title = models.CharField(max_length=100, default=DEFAULT_TITLE)
	location = models.CharField(max_length=100, default=DEFAULT_LOCATION)
	time = models.CharField(max_length=100)
	info = models.TextField(default=DEFAULT_INFO)
	date_created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.time
