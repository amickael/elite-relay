import typing as t

from elite_relay.handlers.base import BaseHandler


class HandlerRegistry:
    def __init__(self):
        self._handlers: dict[str, t.Type[BaseHandler]] = {}

    def register(self, plugin: str, handler: t.Type[BaseHandler]):
        self._handlers[plugin] = handler

    def get(self, plugin: str) -> t.Type[BaseHandler] | None:
        return self._handlers.get(plugin)
