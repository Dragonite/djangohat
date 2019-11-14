from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from .models import Users

from django.http import HttpResponse

@staff_member_required()
def index(request):
    profiles = Users.objects.all()
    c = {'profiles': profiles }
    return render(request, "user_index.html", c)


@login_required
def profile(request):
    user_profile = get_object_or_404(Users, user=request.user)
    c = {'profile': user_profile}
    return render(request, "user_profile.html", c)


@login_required
def confirm_discord(request):
    user_profile = get_object_or_404(Users, user=request.user)
    success = False
    if user_profile.site_verified:
        success = True
    return JsonResponse({"success": success})