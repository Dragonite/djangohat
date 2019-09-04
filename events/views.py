from django.shortcuts import render, redirect
from dhooks import Webhook, Embed
from django.http import HttpResponse
from events.forms import CreateEventForm
from .utils import send_embed
from .models import Event
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.admin.views.decorators import staff_member_required


def index(request):
    current_events = Event.objects.filter(time__gte=timezone.now()).order_by('time')
    previous_events = Event.objects.filter(time__lt=timezone.now()).order_by('time')
    c = {'current_events': current_events, 'previous_events': previous_events}
    return render(request, "index.html", c)


@staff_member_required
def create_event(request):
    form = CreateEventForm()
    if request.POST:
        print(request.POST)
        if request.user.is_staff:
            if CreateEventForm(request.POST).is_valid():
                CreateEventForm(request.POST).save()
                send_embed(request)
                messages.success(request, 'Event created and deployed to Discord!')
                return redirect("events:event_index")
            messages.error(request, 'Invalid Parameters for Event!')
    c = {'form': form }
    return render(request, "create_event.html", c)
