import os
import sys
from django.core.wsgi import get_wsgi_application
sys.path = ['/var/www/myblog'] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'myblog.settings'

application = get_wsgi_application()

