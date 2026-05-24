import requests
from pydantic import BaseModel, HttpUrl

from elite_relay.plugins.base import BasePlugin

__all__ = ['HttpPlugin']


class HttpOptions(BaseModel):
    url: HttpUrl
    headers: dict[str, str] = {}
    query: dict[str, str] = {}


class HttpPlugin(BasePlugin):
    OptionsModel = HttpOptions

    def post(self):
        requests.post(
            url=self.options.url.encoded_string(),
            json=self.entry.model_dump(mode='json'),
            headers=self.options.headers,
            params=self.options.query,
        ).raise_for_status()
