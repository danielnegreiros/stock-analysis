"""

author: @danielnegreiros
"""

import time

from controllers.operation_controller import OperationController
from app_namings import AppDefinition
from utils.utils import AppUtils


def controller():
    """ Text """

    while True:
        # Config data
        app_config = AppUtils.get_app_config(AppDefinition.DEFAULT.value)
        user_config_path = app_config[AppDefinition.USER_CONFIG.value]

        # User config
        user_config = AppUtils.get_yaml_file(user_config_path)
        stocks = user_config[AppDefinition.STOCKS.value]

        # Execution
        for stock in stocks:
            OperationController(stock).start()

        # Sleep for a day
        hour_interval = app_config[AppDefinition.HOUR.value]
        time.sleep(360 * int(hour_interval))


def main():
    """ Text """
    controller()


if __name__ == "__main__":
    main()
