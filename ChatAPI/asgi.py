import os

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator  # new
from chat import routing  # new
from django.core.asgi import get_asgi_application

from .tokenauth_middleware import TokenAuthMiddleware  # new

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChatAPI.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(  # new
        TokenAuthMiddleware(URLRouter(routing.websocket_urlpatterns)))
})
