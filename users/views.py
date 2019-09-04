from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from .models import Users

from django.http import HttpResponse

@staff_member_required()
def index(request):
    users = Users.objects.all()
    c = {'users': users }
    return render(request, "user_index.html", c)