from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
import randomgenerator.routing


application = ProtocolTypeRouter({
    "websocket":AuthMiddlewareStack(
        URLRouter(
            randomgenerator.routing.websocket_urlpatterns,
        ),
    ),
})
