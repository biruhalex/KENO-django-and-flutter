import json
import random

import channels.layers
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class TestConsumer(WebsocketConsumer):

    def websocket_connect(self, message):
        async_to_sync(self.channel_layer.group_add)("msgGroup", self.channel_name)

        self.connect()

        async_to_sync(self.channel_layer.group_send)(
            "msgGroup",
            {
                'type': "echo_msg",
                'msg': "123.55",
            })

    def echo_msg(self, message):
        self.send(json.dumps(message))


def send_msg():
    channel_layer = channels.layers.get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        "msgGroup",
        {
            'type': "echo_msg",
            'msg': str(random.randint(0, 999)),
        })

# celery -A django_channels_example worker -B -l info -n django_channels_example
