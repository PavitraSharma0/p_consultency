import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CONSULT_DIR = os.path.dirname(CURRENT_DIR)

for path in [CONSULT_DIR, CURRENT_DIR]:
    if os.path.exists(path) and path not in sys.path:
        sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'consult.settings')

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
