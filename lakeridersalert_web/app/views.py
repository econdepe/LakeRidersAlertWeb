from django.shortcuts import render

from .models import Session


def index(request):
    calendar_entries = Session.objects.all()

    if len(calendar_entries) == 0:
        return render(request, "app/app_not_started.html")

    return render(
        request,
        "app/wip.html",
    )


def db(request):
    context = {"sessions": Session.objects.all()}

    return render(request, "app/db.html", context)


def alerts(request):
    return render(request, "app/wip.html")
