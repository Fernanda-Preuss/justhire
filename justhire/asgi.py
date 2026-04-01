"""
Configuração ASGI do projeto JustHire.
Expõe a aplicação como a variável 'application'.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "justhire.settings")

application = get_asgi_application()
