from halo import Halo
from seleniumbase import Driver
from zenrows import ZenRowsClient


class BypassCloudflare:
    def init(self, url: str, hints=None, zenrows_token=None):

        self.url = url
        self.hints = hints if hints is not None else ["Один момент", "Just a moment..."]
        self.zenrows_token = zenrows_token

        self.client = None
        self.driver = None

        self.spinner = Halo(text=f"Loading page", spinner='line', color="white", interval=100, placement="right")

        self.connect_zenrows_client() if self.zenrows_token is not None else ...

    def create_webdriver_untdetect(self):
        self.spinner.start("Loading driver")
        self.driver = Driver(uc=True, headless=True)
        self.spinner.succeed()

    def connect_zenrows_client(self):
        self.spinner.start("Connecting Zenrows client")
        self.client = ZenRowsClient(self.zenrows_token)
        self.spinner.succeed()

    def bypass_captcha(self):
        if self.client is None:
            self.create_webdriver_untdetect() if self.driver is None else ...

            self.spinner.start("Getting url")
            self.driver.get(self.url)
            self.spinner.succeed()

            self.spinner.start("Loading page")

            while any(x in self.driver.page_source for x in self.hints):\
                ...

            self.spinner.succeed()

            html = self.driver.page_source
        else:
            self.spinner.start("Getting url")
            response = self.client.get(url, params={"antibot":"true"})
            self.spinner.succeed()
            html = response.text

        return html
