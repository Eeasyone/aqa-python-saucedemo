import allure
import pytest

from src.core.browser import create_driver
from src.config.settings import BASE_URL, DEFAULT_TIMEOUT


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def default_timeout():
    return DEFAULT_TIMEOUT


@pytest.fixture()
def driver(request):
    drv = create_driver()
    yield drv

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        try:
            png = drv.get_screenshot_as_png()
            allure.attach(png, name="screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception:
            pass

    drv.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
