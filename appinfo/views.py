from django.http import JsonResponse
from django.conf import settings
from django.db import connections
from django.db.utils import OperationalError


def info(_request):
    info = settings.APP_INFO
    return JsonResponse(info)


def get_health_check(_request):
    # Verificar la disponibilidad de la aplicación
    health_check = {"app": "ok"}
    # Verificar la conectividad a las base de datos
    db_status = {}
    for conn in connections.all():
        try:
            conn.ensure_connection()
            db_status[conn.alias] = 'ok'
        except OperationalError:
            db_status[conn.alias] = 'unavailable'
    health_check['databases'] = db_status
    return JsonResponse(health_check)