import imp
import os
import sys


sys.path.insert(0, os.path.dirname(__file__))

cwd=os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd+'/malawisociety')
sys.path.insert(0, cwd+'/../venv/bin')
sys.path.insert(0,cwd+'/../venv/lib/python2.7/site-packages/django')
sys.path.insert(0,cwd+'/../venv/lib/python2.7/site-packages')
#wsgi = imp.load_source('wsgi', 'jaffarchiosa/wsgi.py')
#application = wsgi.application

# import jaffarchiosa.wsgi
# application = jaffarchiosa.wsgi.application

from django.core.wsgi import get_wsgi_application

os.environ["DJANGO_SETTINGS_MODULE"] = "logintest.settings_local"

application = get_wsgi_application()
