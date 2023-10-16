import subprocess
from halo import Halo
from seleniumbase import Driver


class BypassCloudflare:
    def __init__(self, url: str, hints=None):

        if hints is None:
            hints = ["Один момент", "Just a moment..."]
        self.url = url
        self.hints = hints

        self.driver = None

        self.spinner = Halo(text=f"Loading page", spinner='line', color="white", interval=100, placement="right", )

    @staticmethod
    def get_chrome_path():
        chrome_path = subprocess.check_output(['which', 'chrome']).decode('utf-8').strip()
        return chrome_path

    def create_webdriver_untdetect(self):
        self.spinner.start("Loading driver")
        self.driver = Driver(uc=True, headless=True)
        self.spinner.succeed()

    def bypass_captcha(self):
        self.create_webdriver_untdetect()

        self.spinner.start("Getting url")
        self.driver.get(self.url)
        self.spinner.succeed("Getting url")

        self.spinner.start("Loading page")

        while any(x in self.driver.page_source for x in self.hints):
            ...

        self.spinner.succeed()

        html = self.driver.page_source

        return html


# url = "https://tokensniffer.com/token/bsc/mkxe928xk6xskz1svaxlbau9ko9lc6i80s6cg3oxz6sulh94g1u6hgkhk96x"

url = "https://pony.town"
bps = BypassCloudflare(url)
print(bps.bypass_captcha())
