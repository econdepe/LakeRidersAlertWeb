from django.http import HttpResponse
from django.shortcuts import render

from .models import Calendar


def index(request):
    calendar_entries = Calendar.objects.all()

    if len(calendar_entries) == 0:
        return render(request, "app/app_not_started.html")

    return render(request, "app/index.html", {})


def db(request):
    return HttpResponse("calendar stored in DB")


def alerts(request):
    return HttpResponse("list of alerts emitted")
