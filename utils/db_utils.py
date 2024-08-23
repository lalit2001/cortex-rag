from typing import List

import pandas
import psycopg2
import snowflake.connector
from snowflake.connector import SnowflakeConnection
import pandas as pd

from utils.config import config

db_config = {
    "host": config.HOST,
    "database": config.DATABASE,
    "user": config.USER,
    "password": config.PASSWORD
}

print(db_config)

# Connect to the database
connection = psycopg2.connect(**db_config)

def get_connection() -> SnowflakeConnection:
    print(config.SF_USER,
       config.SF_PASSWORD,
        config.SF_ACCOUNT)
    ctx = snowflake.connector.connect(
        user=config.SF_USER,
        password=config.SF_PASSWORD,
        account=config.SF_ACCOUNT
    )

    return ctx
def runQuery(connection: SnowflakeConnection, query: str) -> List[dict]:
    cs = connection.cursor()
    try:
        cs.execute(query)
        one_row = cs.fetch_pandas_all()
        return one_row.to_dict(orient='records')
    finally:
        cs.close()

def runPostgresQuery( query: str) -> List[dict]:
    cs = connection.cursor()
    try:
        one_row = pandas.read_sql(query, con=connection)
        return one_row.to_dict(orient='records')
    finally:
        cs.close()
