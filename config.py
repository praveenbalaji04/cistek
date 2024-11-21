import os


def get_env(key, default=None):
    value = os.environ.get(key.upper())
    if value:
        return value
    return default


class Config:
    MONGO_DB_URI = get_env('mongo_db_uri', "localhost:27017")
    MONGO_DB_NAME = get_env('mongo_db_name', "cistek")
