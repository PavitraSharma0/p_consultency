import os
import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
CONSULT_DIR = CURRENT_DIR.parent
ROOT_DIR = CONSULT_DIR.parent

for path in [str(CONSULT_DIR), str(ROOT_DIR)]:
    if os.path.exists(path) and path not in sys.path:
        sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'consult.settings')

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
