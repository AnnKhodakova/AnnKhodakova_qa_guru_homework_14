from models.pages.sign_in import SignInPage


def test_desktop(desktop_window_open):
    sign_in_desktop = SignInPage()
    sign_in_desktop.click_sign_in_desktop()


def test_mobile(mobile_window_open):
    sign_in_mobile = SignInPage()
    sign_in_mobile.click_sign_in_mobile()
