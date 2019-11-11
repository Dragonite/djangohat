from django.core.management.base import BaseCommand
from django.utils import timezone
from events.models import Event

class Command(BaseCommand):
	help = 'Deletes all events in the database. Helpful for testing.'

	def handle(self, *args, **kwargs):
		Event.objects.all().delete()
		self.stdout.write(self.style.SUCCESS('Successfully deleted all events!'))