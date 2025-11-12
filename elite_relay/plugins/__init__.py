from elite_relay.plugins.registry import PluginRegistry

from .browser import BrowserPlugin
from .http import HttpPlugin

registry = PluginRegistry()


# Register plugins below

registry.register('http', HttpPlugin)
registry.register('browser', BrowserPlugin)
