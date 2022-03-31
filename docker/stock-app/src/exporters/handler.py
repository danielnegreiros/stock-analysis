import logging

from exporters.exporter import SqliteExporter
from utils.utils import AppUtils


def get_config(section):
    return AppUtils.get_app_config(section)


class DbHandler:

    @staticmethod
    def export(stock, data):
        """ Exporting to some RDB """

        # Logging
        # Logging
        formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        logging.basicConfig(level=logging.INFO, format=formatter)

        report = data[0]
        schema = data[1]
        mode = data[2]

        date = list(report.keys())[0]
        if not mode == 'fin_data':
            report = report[date]

        config = get_config('DB')
        connection_str = f'{config["type"]}://{config["user"]}:{config["pass"]}@{config["host"]}/{config["name"]}'

        try:
            exporter = SqliteExporter(connection_str,
                                      stock, schema, mode, date, report)
            exporter.export()
        except:
            logging.info(
                f'Exporting failed for {stock} {schema}:{mode}:{date}')
        else:
            logging.info(
                f'Exporting succesfully for {stock} {schema}:{mode}:{date}')
