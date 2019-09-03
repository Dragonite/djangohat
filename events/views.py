from django.shortcuts import render
from dhooks import Webhook, Embed
from django.http import HttpResponse
from events.forms import CreateEventForm
from .utils import send_embed
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def index(request):
    c = {}
    return render(request, "index.html", c)


@login_required
def create_event(request):
    form = CreateEventForm()
    if request.POST:
        print(request.POST)
        if request.user.is_staff:
            if CreateEventForm(request.POST).is_valid():
                CreateEventForm(request.POST).save()
                send_embed(request)

    c = {'form': form }
    return render(request, "index.html", c)
