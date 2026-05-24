import pyperclip
from pydantic import BaseModel

from elite_relay.plugins.base import BasePlugin


class ClipboardOptions(BaseModel):
    text: str
    strip: bool = True


class ClipboardPlugin(BasePlugin):
    OptionsModel = ClipboardOptions

    def copy(self):
        value = self.format_string(self.options.text)
        if self.options.strip:
            value = value.strip()
        pyperclip.copy(value)
