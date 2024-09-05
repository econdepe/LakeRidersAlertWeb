from datetime import datetime
from time import sleep, time
from zoneinfo import ZoneInfo

from .web import (
    create_browser_session,
    get_reservations_html,
    InvalidCredentialsError,
)
from .sessions import (
    extract_calendar_entries,
    find_available_slots,
    write_calendar_entries_to_db,
)

# from .telegram_bot import notify_to_telegram
from app.models import Alert, Session


def run_once(email, password, token, chat_id, session=None, retries=0):
    if retries > 0:
        sleep(2**retries)
    browser_session = create_browser_session() if session is None else session
    try:
        html = get_reservations_html(
            session=browser_session, email=email, password=password
        )
    # TODO: Narrow down error class
    except Exception as e:
        if isinstance(e, InvalidCredentialsError):
            raise e
        # Crete new browser session when retrying to avoid any other type of error (like RemoteDisconnected errors)
        return run_once(
            email=email,
            password=password,
            token=token,
            chat_id=chat_id,
            session=None,
            retries=retries + 1,
        )

    calendar_entries = extract_calendar_entries(html)
    slots = find_available_slots(calendar_entries)
    if slots is not None:
        # notify_to_telegram(available_slots=slots, token=token, chat_id=chat_id)
        timestamp = int(time())
        for datetime, count in slots.items():
            Alert.objects.create(
                session=Session.objects.get(datetime=datetime),
                timestamp=timestamp,
                count=count,
            )
    write_calendar_entries_to_db(calendar_entries)

    return browser_session


# Polling should be run only between 7am and midnight
def run_once_conditionally(email, password, token, chat_id, session=None):
    now = datetime.now(ZoneInfo("Europe/Zurich"))
    if now.hour >= 7:
        return run_once(
            email=email,
            password=password,
            token=token,
            chat_id=chat_id,
            session=session,
        )
    else:
        return session
