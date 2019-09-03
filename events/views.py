from django.shortcuts import render
from dhooks import Webhook, Embed
from django.http import HttpResponse
from django.conf import settings

hook = Webhook(settings.DISCORD_WEBHOOK)

def index(request):
    c = {}
    return render(request, "index.html", c)


def create_event(request):
    if request.POST:
        print(request.POST)
        hook.send(request.POST['test'])
    c = {}
    return render(request, "index.html", c)
