import logging

from utils.utils import AppUtils
from scraper.errors import ScrapeError


class ParserValidator:

    def __init__(self, stock, reports) -> None:
        self.stock = stock
        self.reports = reports

    def parsing_logging(self, schema, mode, result) -> None:
        if result:
            logging.info(
                f'Parsing succesfully for {self.stock} {schema}:{mode}')
        else:
            logging.error(f'Parsing failed for {self.stock} {schema}:{mode}')

    def prepare_export(self):
        """ Check if data coming from scraper is valid
        and consistent """

        # Logging
        formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        logging.basicConfig(level=logging.INFO, format=formatter)

        # List to hold consistent data after chekckings
        prepared_data_list = []

        schema_path = AppUtils.get_user_config_param('APP', 'schema')
        schemas = AppUtils.get_yaml_file(schema_path)['schemas']

        for schema, mode in schemas.items():

            # If no future exceptions are found
            # result of the operation will be success (True)
            result = True
            try:
                report_events = self.reports[mode][schema][self.stock]
                # Check if report coming from scraping is valid
                if report_events is None:
                    raise ScrapeError

            except ConnectionResetError:
                result = False
                logging.error(
                    f'Scraping failed for {self.stock} {schema}:{mode} - ConnectionResetError')

            except KeyError:
                result = False
                logging.error(
                    f'Scraping failed for {self.stock} {schema}:{mode} - KeyError')

            except ScrapeError:
                result = False
                logging.error(
                    f'Scraping failed for {self.stock} {schema}:{mode} - Parsing')

            else:
                # If no errors are found append data to consistent
                # data list
                for report in report_events:
                    prepared_data_list.append((report, schema, mode))

            finally:
                self.parsing_logging(schema, mode, result)

        if 'fin_data' in self.reports and self.stock in self.reports['fin_data']:
            prepared_data_list.append(
                (self.reports['fin_data'][self.stock], 'fin_data', 'fin_data'))

        return prepared_data_list
