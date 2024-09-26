from typing import Any, Generator

import pytest

from main import App


# Fixture pro inicializaci hlavní aplikace
@pytest.fixture
def app_init() -> Generator:
    app: App = App("mapibase", 1024, 768)
    yield app
    app.quit()
