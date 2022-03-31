"""_summary_
"""

import logging
import threading

from scraper.framework_scraper import YahooScraper

from app_namings import AppDefinition
from utils.utils import AppUtils
from exporters.handler import DbHandler
from scraper.validator import ParserValidator


class OperationController(threading.Thread):

    # Use semaphore to limit the number of concurrent threads
    semaphore_value = int(AppUtils.get_user_config_param(
        'DEFAULT', AppDefinition.SEMAPHORE.value))
    semaphore = threading.BoundedSemaphore(semaphore_value)

    def __init__(self, stock) -> None:
        self.stock = stock
        super().__init__()

    def run(self):
        """ Start Execution """

        formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        logging.basicConfig(level=logging.INFO, format=formatter)

        self.semaphore.acquire()
        logging.info('Starting: {}'.format(self.stock))

        # Chosse wether we are going to use yahoo financial module
        # or some customized scraper
        scraper = YahooScraper(self.stock)
        data = scraper.scrape_data()

        # Export it to sql db
        validator = ParserValidator(self.stock, data)
        prepared_data_list = validator.prepare_export()

        for data in prepared_data_list:
            DbHandler.export(self.stock, data)

        self.semaphore.release()
        logging.info('Finished: {}'.format(self.stock))
