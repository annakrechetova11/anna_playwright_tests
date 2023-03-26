from playwright.sync_api import sync_playwright


class Browsers(object):
    def __init__(self):
        self.page = None
        self.context = None

    def invoke_chrome_browser(self):
        driver = sync_playwright().start().chromium.launch(headless=False, channel='chrome', args=['--start-maximized'])
        # driver.new_context()
        page = driver.new_page(no_viewport=True)
        self.page = page
        self.context = driver.contexts[0]

    def navigate_to_page(self, url):
        self.page.goto(url)
