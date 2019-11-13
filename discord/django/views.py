from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from users.models import Users
from pathlib import Path

from django.http import HttpResponse

@staff_member_required()
def bot_landing(request):
    contents = Path('discord/logs/whitehat.log').read_text()
    c = {}
    return render(request, "discord/landing.html", c)