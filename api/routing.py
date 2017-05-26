from api import socketconsumers
from channels.routing import route

channel_routing = [
    route('websocket.receive', socketconsumers.ws_message),
    route('websocket.disconnect', socketconsumers.ws_disconnect),
]
