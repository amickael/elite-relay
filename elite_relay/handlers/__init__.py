from elite_relay.handlers.registry import HandlerRegistry

from .browser import BrowserHandler
from .http import HttpHandler

registry = HandlerRegistry()


# Register handlers below

registry.register('http', HttpHandler)
registry.register('browser', BrowserHandler)
