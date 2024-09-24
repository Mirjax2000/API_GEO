from typing import Any, Generator
import pytest

from main import App


# Fixture pro inicializaci hlavní aplikace
@pytest.fixture
def app_init() -> Generator[App, Any, None]:
    app = App()
    yield app
    app.quit()
