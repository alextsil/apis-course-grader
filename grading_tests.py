import requests

from logger import Logger
from result import Result
from settings import Settings

logger = Logger().logger


class GradingTests:

    def get_all(self):
        r = requests.get(Settings.ws_conn_string + '/tweets')
        print(r.status_code)
        print(r.content)
        res = Result(True, "tsikos")
        return res
