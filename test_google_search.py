from selene import be, have
from selene.support.shared import browser


def test_search_no_empty_result(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    assert browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in ...')), 'Проверка верных результатов поиска'


def test_search_empty_result(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('KKDKDMK J3OERJ Q2E4').press_enter()
    assert browser.element('#result-stats').should(have.text('About 0 results')), 'Проверка на пустой результат поиска'
