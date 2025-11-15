from elite_relay.plugins.registry import PluginRegistry

from .browser import BrowserPlugin
from .clipboard import ClipboardPlugin
from .http import HttpPlugin

registry = PluginRegistry()


# Register plugins below

registry.register('http', HttpPlugin)
registry.register('browser', BrowserPlugin)
registry.register('clipboard', ClipboardPlugin)
