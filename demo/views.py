import logging
from time import sleep

from django.db import transaction
from django.http import JsonResponse
from django.views.generic.base import View

from demo.models import SomeItem

logger = logging.getLogger(__name__)


def create_and_count_items(seconds_delay):
    with transaction.atomic():
        # create 19 items
        for i in range(0, 19):
            SomeItem.objects.create()
        # delay execution
        sleep(seconds_delay)
        # create the last item
        SomeItem.objects.create()
        item_count = SomeItem.objects.count()
        return item_count


def sanitize_sleep_parameter(request):
    """
    Limits the sleep-parameter to values between 0 and 120 seconds.
    """
    value = float(request.GET.get('sleep', default=1))
    return min(abs(value), 120)


class BlockingTransationView(View):
    """
    This creates several items in a transaction with a configurable delay.

    The delay (in seconds) can be specified with the GET-parameter 'sleep' (limited
    to values between 0 and 120 seconds). Default is 1 second delay.

    :returns a JsonResponse with some delay in seconds and the total item count
    """

    def get(self, request, *args, **kwargs):
        seconds_delay = sanitize_sleep_parameter(request)
        try:
            total_item_count = create_and_count_items(seconds_delay)
            data = {
                'seconds_delay': seconds_delay,
                'total_item_count': total_item_count,
            }
            return JsonResponse(data=data)
        except Exception as e:
            raise e
