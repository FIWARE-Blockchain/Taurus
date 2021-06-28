#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from configparser import ConfigParser

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taurus.settings')


    #Read config.ini file    
    config_file = os.path.join('.', 'apis' , 'config.ini')

    print(config_file)

    config_object = ConfigParser()
    config_object.read(config_file)
    config_object.sections()

    taurus_info = config_object["TAURUS"]

    port = taurus_info["port"]

    # Override default port for `runserver` command
    from django.core.management.commands.runserver import Command as runserver
    runserver.default_port = port

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()