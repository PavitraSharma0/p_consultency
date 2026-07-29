import os
import sys

# Add project root and consult directories to Python path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(CURRENT_DIR)
CONSULT_DIR = os.path.join(ROOT_DIR, 'consult')

for path in [CONSULT_DIR, ROOT_DIR]:
    if os.path.exists(path) and path not in sys.path:
        sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'consult.settings')

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
