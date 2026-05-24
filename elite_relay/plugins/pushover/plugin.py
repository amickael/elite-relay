import typing as t

import requests
from pydantic import BaseModel, HttpUrl, PositiveInt

from elite_relay.plugins.base import BasePlugin


class PushoverOptions(BaseModel):
    api_token: str
    user_key: str
    message: str
    title: str | None = None
    priority: int | None = None
    sound: str | None = None
    ttl: PositiveInt | None = None
    endpoint: HttpUrl = HttpUrl('https://api.pushover.net/1/messages.json')


class PushoverPlugin(BasePlugin):
    OptionsModel = PushoverOptions

    def notify(self):
        payload: dict[str, t.Any] = {
            'token': self.options.api_token,
            'user': self.options.user_key,
            'message': self.format_string(self.options.message),
        }
        if self.options.title is not None:
            payload['title'] = self.format_string(self.options.title)
        if self.options.priority is not None:
            payload['priority'] = self.options.priority
        if self.options.sound is not None:
            payload['sound'] = self.options.sound
        if self.options.ttl is not None:
            payload['ttl'] = self.options.ttl
        requests.post(
            url=self.options.endpoint.encoded_string(),
            data=payload,
        ).raise_for_status()
