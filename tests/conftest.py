import datetime as dt
from pathlib import Path

import pytest


@pytest.fixture(scope='session')
def data_dir():
    return Path(__file__).parent / 'data'


@pytest.fixture
def format_timestamp():
    def _format_timestamp(ts: dt.datetime) -> str:
        return ts.strftime('%Y-%m-%dT%H:%M:%SZ')

    yield _format_timestamp


@pytest.fixture
def get_timestamp(format_timestamp):
    def _get_timestamp() -> str:
        return format_timestamp(dt.datetime.now(tz=dt.timezone.utc))

    yield _get_timestamp
