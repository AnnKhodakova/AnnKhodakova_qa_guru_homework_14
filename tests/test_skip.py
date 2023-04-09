import pytest

from models.pages.sign_in import SignInPage


@pytest.mark.parametrize(
    "browser_open",
    [
        pytest.param("desktop"),
        pytest.param("mobile", marks=[pytest.mark.skip(reason="This test is for desktop")]),
    ],
    indirect=True,
)
def test_desktop(browser_open):
    sign_in_desktop = SignInPage()
    sign_in_desktop.click_sign_in_desktop()


@pytest.mark.parametrize(
    "browser_open",
    [
        pytest.param("mobile"),
        pytest.param("desktop", marks=[pytest.mark.skip(reason="This test is for mobile")]),
    ],
    indirect=True,
)
def test_mobile(browser_open):
    sign_in_mobile = SignInPage()
    sign_in_mobile.click_sign_in_mobile()
