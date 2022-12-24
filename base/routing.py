from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path(r"ws/chat", consumers.ChatRoomConsumer.as_asgi())
]