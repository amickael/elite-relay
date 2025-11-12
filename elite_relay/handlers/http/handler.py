import requests
from pydantic import BaseModel, HttpUrl

from elite_relay.handlers.base import BaseHandler

__all__ = ['HttpHandler']


class HttpOptions(BaseModel):
    url: HttpUrl
    headers: dict[str, str] = {}
    query: dict[str, str] = {}


class HttpHandler(BaseHandler):
    def post(self):
        options = HttpOptions.model_validate(self.config.options)
        requests.post(
            url=options.url.encoded_string(),
            json=self.entry.model_dump(mode='json'),
            headers=options.headers,
            params=options.query,
        ).raise_for_status()
