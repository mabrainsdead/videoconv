"""
WSGI config for videoconvProj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os,sys

path = "/var/www/html/videoconv"

if path not in sys.path:
	sys.path.insert(0,path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'videoconvProj.settings')

application = get_wsgi_application()
