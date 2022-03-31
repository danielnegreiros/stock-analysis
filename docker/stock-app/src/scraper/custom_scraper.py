from scraper.abc_scraper import Scraper


class CustomScraper(Scraper):

    def __init__(self, ticker) -> None:
        super().__init__(ticker)

    def scrape_data(self):
        pass
