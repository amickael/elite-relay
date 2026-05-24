import logging
import re
import typing as t
from abc import ABC
from functools import cached_property

from pydantic import AnyUrl, BaseModel

from elite_relay.journal import JournalEntry
from elite_relay.settings import PluginConfig

T = t.TypeVar("T", bound=BaseModel)


class BasePlugin(ABC, t.Generic[T]):
    OptionsModel: t.Type[T] | None = None
    RE_PARAMS = re.compile(r'\${([a-zA-Z0-9._-]+)}')

    def __init__(self, entry: JournalEntry, config: PluginConfig):
        self.entry = entry
        self.config = config

    @cached_property
    def options(self) -> T:
        if self.OptionsModel:
            return self.OptionsModel.model_validate(self.config.options)
        raise ValueError('OptionsModel is undefined')

    def format_string(self, value: str | AnyUrl) -> str:
        if isinstance(value, AnyUrl):
            value = value.unicode_string()
        for match in self.RE_PARAMS.finditer(value):
            if (tpl := match.group()) not in value:
                continue
            if (repl := self.entry.search(match.group(1))) is None:
                continue
            value = value.replace(tpl, repl)
        return value

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
