import datetime
from dateutil import tz
from django.conf import settings


SYSTEM_TZ = tz.gettz(settings.TIME_ZONE)


def get_current_datetime():
    return datetime.datetime.now(tz=SYSTEM_TZ)
