from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from django.http import HttpResponse

@staff_member_required
def index(request):
    return HttpResponse("Hello, world. You're at the users index.")