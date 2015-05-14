"""
WSGI config for phoenixcs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
#/var/www/phoenixcs.ru:
#                /root/Envs/phoenixcs/lib/python2.7/site-packages
site.addsitedir('/root/Envs/phoenixcs/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/var/www/phoenixcs.ru')
sys.path.append('/var/www/phoenixcs.ru/phoenixcs')



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "phoenixcs.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
