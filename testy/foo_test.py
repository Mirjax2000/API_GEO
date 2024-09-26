from time import sleep
from typing import Any, Generator

import pytest

from main import App


def test_app_ini(app_init: App) -> None:
    result: App = app_init
    sleep(0.1)
    assert isinstance(result, App), "Instance App nebezi"


# def test_instance_running(app_init: App) -> None:
#     try:
#         result: MainFrame = app_init.main_frame
#         assert isinstance(result, MainFrame), "Instance MainFrame nebezi"
#     except Exception as e:
#         assert isinstance(e, AssertionError), f"problim: {e}"
