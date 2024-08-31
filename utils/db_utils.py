from typing import List

import pandas
import snowflake.connector
from snowflake.connector import SnowflakeConnection

from utils.config import config

db_config = {
    "host": config.HOST,
    "database": config.DATABASE,
    "user": config.USER,
    "password": config.PASSWORD
}

print(db_config)

connection = "psycopg2.connect(**db_config)"

def get_connection() -> SnowflakeConnection:
    snowflake_account = config.SF_ACCOUNT
    snowflake_user = config.SF_USER
    snowflake_password = config.SF_PASSWORD
    snowflake_warehouse = 'COMPUTE_WH'
    snowflake_database = 'RAG_DEMO'
    snowflake_schema = 'PUBLIC'

    ctx = snowflake.connector.connect(
        user=snowflake_user,
        password=snowflake_password,
        account=snowflake_account,
        warehouse=snowflake_warehouse,
        database=snowflake_database,
        schema=snowflake_schema
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


def runSnowfakeQuery(query: str) -> List[dict]:

    conn: SnowflakeConnection = get_connection()
    cs = conn.cursor()
    try:

        cs.execute(query)
        df = cs.fetch_pandas_all()
        return df.to_dict(orient='records')
    finally:
        cs.close()
