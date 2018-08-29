import pymongo

from settings import Settings


class Db:

    def __init__(self):
        self.db = pymongo.MongoClient(Settings.db_conn_string)["apis"]["apis"]

    def find_all(self):
        return self.db.find({})

    def find_with_hashtags_more_than(self, more_than):
        return self.db.find({('entities.hashtags.' + str(more_than)): {'$exists': True}})

    def find_with_hashtags(self, hashtag):
        return self.db.find({'entities.hashtags.text': hashtag})
