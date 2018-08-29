import json

import requests

from db import Db
from logger import Logger
from result import Result
from settings import Settings

logger = Logger().logger
db = Db()


class GradingTests:

    def get_all_normal_count(self):
        results = []
        assignment = "Get request on /tweets"

        try:
            r = requests.get(Settings.ws_conn_string + '/tweets')

            if r.status_code == 200:
                results.append(Result(True, assignment, "Status code was 200"))
            else:
                results.append(Result(False, assignment, "Status code was not 200. Was " + str(r.status_code)))

            all_db_count = db.find_all().count()
            mapped_json_count = len(json.loads(r.content))
            if all_db_count == mapped_json_count:
                results.append(Result(True, assignment, "Our db count matched your returned count"))
            else:
                results.append(Result(False, assignment,
                                      "Our db count was: " + str(all_db_count)
                                      + ". Your service returned: " + str(mapped_json_count)))

        except requests.exceptions.RequestException as e:
            logger.warn(e)
            results.append(Result(False, assignment, e))

        return results
