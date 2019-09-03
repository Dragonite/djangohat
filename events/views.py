from django.shortcuts import render
from dhooks import Webhook, Embed
from django.http import HttpResponse
from events.forms import CreateEventForm
from .utils import send_embed

def index(request):
    c = {}
    return render(request, "index.html", c)


def create_event(request):
    form = CreateEventForm()
    if request.POST:
        print(request.POST)
        if CreateEventForm(request.POST).is_valid():
            CreateEventForm(request.POST).save()
            send_embed(request)

    c = {'form': form }
    return render(request, "index.html", c)
