import json

from scraper.abc_scraper import Scraper
from yahoofinancials import YahooFinancials


class YahooScraper(Scraper):

    def __init__(self, ticker) -> None:
        super().__init__(ticker)

    def scrape_data(self):

        data = {}

        # with open('./src/debug/report.json') as file_:
        #     data = json.load(file_)

        yahoo_financials = YahooFinancials(self.ticker)
        data['anual'] = yahoo_financials.get_financial_stmts(
            'annual', ['income', 'cash', 'balance'])

        data['quarterly'] = yahoo_financials.get_financial_stmts(
            'quarterly', ['income', 'cash', 'balance'])

        data['fin_data'] = yahoo_financials.get_stock_data(
            statement_type='keystats', tech_type='financialData')

        return data
