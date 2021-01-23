from django.conf import settings


def is_basic_mode():
    return settings.WALDUR_OPENNEBULA.get('BASIC_MODE')
