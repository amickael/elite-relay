import logging
from abc import ABC

from elite_relay.journal import JournalEntry
from elite_relay.settings import PluginConfig


class BasePlugin(ABC):
    def __init__(self, entry: JournalEntry, config: PluginConfig):
        self.entry = entry
        self.config = config

    def handle(self) -> bool:
        for filter_ in self.config.filters:
            if (value := self.entry.search(filter_.key)) is None:
                return False
            if not filter_.compare(value):
                return False
        if not callable(method := getattr(self, self.config.action, None)):
            logging.warning(
                f'Invalid action "{self.config.action}" for plugin "{self.config.plugin}"'
            )
            return False
        method()
        return True
