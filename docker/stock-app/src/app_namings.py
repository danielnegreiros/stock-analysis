from enum import Enum


class AppDefinition(Enum):

    USER_CONFIG = 'user_config'
    STOCKS = 'stocks'
    SEMAPHORE = 'semaphore'
    DEFAULT = 'DEFAULT'
    HOUR = 'hour_interval'
