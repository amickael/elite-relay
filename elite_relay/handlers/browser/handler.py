import typing as t
import webbrowser

from pydantic import BaseModel, HttpUrl

from elite_relay.handlers.base import BaseHandler

__all__ = ['BrowserHandler']

OpenMethod = t.Literal['default', 'window', 'tab']
_open_method_map: dict[OpenMethod, int] = {
    'default': 0,
    'window': 1,
    'tab': 2,
}


class BrowserOptions(BaseModel):
    url: HttpUrl
    params: dict[str, str] = {}
    focus: bool = False
    open_method: OpenMethod = 'default'


class BrowserHandler(BaseHandler):
    def open(self):
        options = BrowserOptions.model_validate(self.config.options)
        params: dict[str, str] = {}
        for param, path in options.params.items():
            if (value := self.entry.search(path)) is None:
                continue
            params[param] = value
        webbrowser.open(
            url=options.url.unicode_string().format(**params),
            new=_open_method_map[options.open_method],
            autoraise=options.focus,
        )
