import logging
from pathlib import Path

from django.conf import settings

logger = logging.getLogger('metrics')


class MetricsMiddleware:
    total_requests = 0
    status_2xx = 0
    status_4xx = 0
    status_5xx = 0

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        MetricsMiddleware.total_requests += 1
        response = self.get_response(request)
        status = response.status_code

        if 200 <= status < 300:
            MetricsMiddleware.status_2xx += 1
        elif 400 <= status < 500:
            MetricsMiddleware.status_4xx += 1
        elif 500 <= status < 600:
            MetricsMiddleware.status_5xx += 1

        message = (
            f'Total requests: {MetricsMiddleware.total_requests}, '
            f'2xx: {MetricsMiddleware.status_2xx}, '
            f'4xx: {MetricsMiddleware.status_4xx}, '
            f'5xx: {MetricsMiddleware.status_5xx}'
        )
        print(message)
        logger.info(message)
        return response
