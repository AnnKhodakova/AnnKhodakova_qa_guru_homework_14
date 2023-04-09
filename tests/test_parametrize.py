import pytest

from models.pages.sign_in import SignInPage


@pytest.mark.parametrize("browser_open", ['desktop'], indirect=True)
def test_desktop(browser_open):
    sign_in_desktop = SignInPage()
    sign_in_desktop.click_sign_in_desktop()


@pytest.mark.parametrize("browser_open", ['mobile'], indirect=True)
def test_mobile(browser_open):
    sign_in_mobile = SignInPage()
    sign_in_mobile.click_sign_in_mobile()
