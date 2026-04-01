"""
Configuração WSGI do projeto JustHire.
Expõe a aplicação como a variável 'application'.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "justhire.settings")

application = get_wsgi_application()
