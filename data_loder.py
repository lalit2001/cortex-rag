import snowflake.connector
import pandas as pd

from utils.config import config


snowflake_account = config.SF_ACCOUNT
snowflake_user = config.SF_USER
snowflake_password = config.SF_PASSWORD
snowflake_warehouse = 'COMPUTE_WH'
snowflake_database = 'RAG_DEMO'
snowflake_schema = 'PUBLIC'


file_paths = {
    'users': 'data/users.csv',
    'payments': 'data/payments.csv',
    'settlements': 'data/settlements.csv',
    'disputes': 'data/disputes.csv',
    'financial_data': 'data/financial_data.csv'
}


table_creation_sql = {
    'users': """
        CREATE OR REPLACE TABLE users (
            user_id STRING,
            user_name STRING,
            user_email STRING,
            user_phone STRING
        );
    """,
    'payments': """
        CREATE OR REPLACE TABLE payments (
            payment_id STRING,
            user_id STRING,
            amount FLOAT,
            payment_date DATE,
            status STRING
        );
    """,
    'settlements': """
        CREATE OR REPLACE TABLE settlements (
            settlement_id STRING,
            payment_id STRING,
            settlement_date DATE,
            amount_settled FLOAT,
            settlement_status STRING
        );
    """,
    'disputes': """
        CREATE OR REPLACE TABLE disputes (
            dispute_id STRING,
            payment_id STRING,
            dispute_date DATE,
            dispute_reason STRING,
            dispute_status STRING
        );
    """,
    'financial_data': """
        CREATE OR REPLACE TABLE financial_data (
            financial_data_id STRING,
            user_id STRING,
            data_date DATE,
            financial_metric STRING,
            value FLOAT
        );
    """
}

conn = snowflake.connector.connect(
    user=snowflake_user,
    password=snowflake_password,
    account=snowflake_account,
    warehouse=snowflake_warehouse,
    database=snowflake_database,
    schema=snowflake_schema
)


def create_table_if_not_exists(table_name):
    """Create table in Snowflake if it does not already exist."""
    create_table_sql = table_creation_sql.get(table_name)
    if create_table_sql:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        print(f"Table {table_name} created or replaced.")
    else:
        print(f"No table creation SQL found for {table_name}.")


def insert_df_into_snowflake(df, table_name):
    """Insert data from DataFrame into Snowflake table."""

    columns = ', '.join(df.columns)
    values = ', '.join(['%s'] * len(df.columns))


    insert_sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"


    cursor = conn.cursor()


    for row in df.itertuples(index=False):
        cursor.execute(insert_sql, row)

    print(f"Data from DataFrame inserted into {table_name}.")



for table_name, file_path in file_paths.items():
    create_table_if_not_exists(table_name)
    df = pd.read_csv(file_path)
    insert_df_into_snowflake(df, table_name)


conn.close()