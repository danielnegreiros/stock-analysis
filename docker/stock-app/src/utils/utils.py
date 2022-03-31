"""_summary_

Returns:
    _type_: _description_

@author: @danielnegreiros
"""

import yaml
import configparser


class AppUtils:


    @staticmethod
    def get_user_config_param(section, param):
        """ Text """
        parser = configparser.ConfigParser()
        parser.read('src/config/app_config.conf')

        return (parser.get(section, param))

    @staticmethod
    def get_yaml_file(path):
        """ Text """
        with open(path) as file_:
            return yaml.safe_load(file_)

    @staticmethod
    def get_app_config(section):
        """ Text """

        path = 'src/config/app_config.conf'
        parser = configparser.ConfigParser()
        parser.read(path)

        return (dict(parser.items(section)))
