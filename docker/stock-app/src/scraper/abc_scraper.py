from abc import ABC, abstractmethod


class Scraper(ABC):

    def __init__(self, ticker) -> None:
        self.ticker = ticker
        super().__init__()

    @abstractmethod
    def scrape_data(self):
        pass
