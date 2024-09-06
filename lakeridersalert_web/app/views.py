import pendulum
from django.shortcuts import render

from .models import Session


def _build_current_week_context(sessions):
    # Build datetime string for days of current week
    now = pendulum.now()
    week_start = now.start_of("week")
    base_dates = [(week_start.add(days=i)).strftime("%Y-%m-%d") for i in range(5)]
    context = {"hours": {}}
    for hour in ["18", "19", "20"]:
        row = []
        for date in base_dates:
            try:
                members = sessions.get(datetime=f"{date}T{hour}").members
            except Session.DoesNotExist:
                members = "EMPTY"
            row.append(members.replace(",", ", "))
        context["hours"][hour] = row

    return context


def index(request):
    sessions = Session.objects.all()

    if len(sessions) == 0:
        return render(request, "app/app_not_started.html")

    context = _build_current_week_context(sessions)

    return render(request, "app/index.html", context)


def db(request):
    context = {"sessions": Session.objects.all()}

    return render(request, "app/db.html", context)


def alerts(request):
    return render(request, "app/wip.html")
