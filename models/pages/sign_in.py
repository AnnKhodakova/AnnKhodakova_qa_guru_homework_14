from selene.support.shared import browser


class SignInPage:

    def click_sign_in_desktop(self):
        browser.element('.HeaderMenu-link--sign-up').click()
        return self

    def click_sign_in_mobile(self):
        browser.elements('.Button-label').first.click()
        return self
