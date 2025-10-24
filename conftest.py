# import pytest
# from playwright.sync_api import sync_playwright
#
#
# @pytest.fixture(scope="session", autouse=True)
# def install_browsers():
#     # Убедиться, что браузеры установлены (нужен playwright в venv)
#     # Запускается единожды за сессию.
#     import subprocess, sys
#     subprocess.run([sys.executable, "-m", "playwright", "install"], check=True)
#
# # pytest-playwright предоставляет fixtures page, browser и т.д.
# # Никаких дополнительных фикстур не требуется для простого набора тестов.
#
