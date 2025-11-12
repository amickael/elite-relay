import logging
import threading
import time

from elite_relay.handlers import registry
from elite_relay.journal import JournalEntry, JournalMonitor
from elite_relay.settings import Settings

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=Settings.read().log_level,
    datefmt='%Y-%m-%d %H:%M:%S',
)


class App:
    def __init__(self):
        self.monitor = JournalMonitor(self.settings.logs_dir)
        self._stop = threading.Event()

    @property
    def settings(self) -> Settings:
        return Settings.read()

    def handle_entry(self, entry: JournalEntry):
        for handler_config in self.settings.handlers:
            handler_cls = registry.get(handler_config.plugin)
            if not handler_cls:
                logging.warning(f'Invalid plugin "{handler_config.plugin}"')
                continue
            handler_obj = handler_cls(entry, handler_config)
            # noinspection PyBroadException
            try:
                result = handler_obj.handle()
            except Exception:
                result = False
                logging.exception(
                    f'Plugin "{handler_config.plugin}" failed to handle {entry}'
                )
            if result:
                logging.info(f'Plugin "{handler_config.plugin}" handled {entry}')
                time.sleep(self.settings.event_interval)

    def start(self):
        while not self._stop.is_set():
            try:
                for entry in self.monitor.iter_entries():
                    self.handle_entry(entry)
                    logging.debug(f'Processed {entry}')
                time.sleep(self.settings.poll_interval)
            except KeyboardInterrupt:
                self.stop()

    def stop(self):
        self._stop.set()


if __name__ == '__main__':
    App().start()
