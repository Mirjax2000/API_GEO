import pytest
from time import sleep

from main import App, MainFrame
from typing import Any, Generator


def test_app_ini(app_init: App) -> None:
    result: App = app_init
    sleep(0.1)
    assert isinstance(result, App), "Instance App nebezi"


def test_instance_running(app_init: App) -> None:
    try:
        result: MainFrame = app_init.main_frame
        assert isinstance(result, MainFrame), "Instance MainFrame nebezi"
    except Exception as e:
        assert isinstance(e, AssertionError), f"problim: {e}"

