import pymongo

from settings import Settings


class Db:

    def __init__(self):
        self.db = pymongo.MongoClient(Settings.db_conn_string)["apis"]["apis"]

    def find_all(self):
        return self.db.find({}, no_cursor_timeout=True)
