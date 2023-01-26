#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from apps.registro.utils import instanciar1, instanciar2
from django.conf import settings


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'heimdallMetric.settings.local2')
    try:
        from django.core.management import execute_from_command_line
        # instanciar influxdb
        if settings.CONFIG_SEL == 1:
            instanciar1()  # config contenedor de juan
        else:
            instanciar2()  # config fede test
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
