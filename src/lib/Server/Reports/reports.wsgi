import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'Bcfg2.Server.Reports.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
