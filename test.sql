USE ROLE ACCOUNTADMIN;

CREATE ROLE cortex_user_role;
GRANT DATABASE ROLE SNOWFLAKE.CORTEX_USER TO ROLE cortex_user_role;

GRANT ROLE cortex_user_role TO USER BUDHISMITA;

SELECT *
  FROM SNOWFLAKE.ACCOUNT_USAGE.METERING_DAILY_HISTORY
  WHERE SERVICE_TYPE='AI_SERVICES';



RAG_DEMO.PUBLIC.USERS


SELECT SYSTEM$ALLOWLIST();

SELECT SYSTEM$ALLOWLIST_PRIVATELINK();

GRANT DATABASE SNOWFLAKE


create database RAG_DEMO












SELECT SNOWFLAKE.CORTEX.COMPLETE('snowflake-arctic', '         You are a Senior SnowSQL Developer working with a Snowflake Data Warehouse.          Instructions:         - Break down the user query into smaller, more manageable steps. Follow the reasoning instructions steps below.         - Use relevant columns from the context given below to filter and subset the data for each step.         - Plan the final SnowSQL query based on the user"s intent.         - After planned the snowflake sql query and based on the user query, decide which visualization chart will be         more suitable to represent the output of the snow sql query. Choose from the supported visualization charts         given below. Pick the chart from below list only as it is and send back the output.         - Pick the colums from the given context below only. Dont construct the query with the attributes that"s not          provided in the context. Context information is something you need to understand, then analyze the context          information with the user query and then plan, build the snow_sql query.         - Follow the output parser format. The result should be returned in the specified format only.          Check the below sample query examples how user needs the output.                  output parser format:         {"snowflakeQuery": <class "str">, "chartType": <class "str">, "userQuestion": <class "str">}                  supported visualization charts:         ["bar_chart", "pie_chart", "line_chart", "histogram", "text", "area_chart"]                  context:         {"settlement_summary_daily": {"columns": [{"name": "id", "type": "bigint"}, {"name": "partner_source_id", "type": "integer"}, {"name": "date", "type": "date"}, {"name": "month", "type": "integer"}, {"name": "year", "type": "integer"}, {"name": "sum_settlement", "type": "numeric"}, {"name": "count_settlement", "type": "integer"}, {"name": "ledger_account_id", "type": "character varying"}, {"name": "institution_account_id", "type": "character varying"}, {"name": "partner_account_id", "type": "character varying"}, {"name": "partner_source", "type": "character varying"}, {"name": "live_connection", "type": "character varying"}, {"name": "sum_settlement_currency", "type": "character varying"}], "relationships": []}, "settlement_summary_monthly": {"columns": [{"name": "id", "type": "bigint"}, {"name": "partner_source_id", "type": "integer"}, {"name": "month", "type": "integer"}, {"name": "year", "type": "integer"}, {"name": "sum_settlement", "type": "numeric"}, {"name": "count_settlement", "type": "integer"}, {"name": "live_connection", "type": "character varying"}, {"name": "ledger_account_id", "type": "character varying"}, {"name": "institution_account_id", "type": "character varying"}, {"name": "partner_account_id", "type": "character varying"}, {"name": "partner_source", "type": "character varying"}, {"name": "sum_settlement_currency", "type": "character varying"}], "relationships": []}, "settlement_summary_yearly": {"columns": [{"name": "id", "type": "bigint"}, {"name": "partner_source_id", "type": "integer"}, {"name": "year", "type": "integer"}, {"name": "sum_settlement", "type": "numeric"}, {"name": "count_settlement", "type": "integer"}, {"name": "live_connection", "type": "character varying"}, {"name": "sum_settlement_currency", "type": "character varying"}, {"name": "ledger_account_id", "type": "character varying"}, {"name": "institution_account_id", "type": "character varying"}, {"name": "partner_account_id", "type": "character varying"}, {"name": "partner_source", "type": "character varying"}], "relationships": []}, "ledger_account_settlement": {"columns": [{"name": "id", "type": "character varying"}, {"name": "object", "type": "character varying"}], "relationships": []}, "ledger_account_relation_settlement": {"columns": [{"name": "ledger_account_id", "type": "character varying"}, {"name": "settlement_id", "type": "character varying"}], "relationships": [{"column": "settlement_id", "foreign_table": "settlement", "foreign_column": "id"}, {"column": "ledger_account_id", "foreign_table": "ledger_account_settlement", "foreign_column": "id"}]}, "settlement": {"columns": [{"name": "amount", "type": "numeric"}, {"name": "modified_date", "type": "bigint"}, {"name": "scheduled", "type": "boolean"}, {"name": "partner_account_connection_id", "type": "bigint"}, {"name": "partner_source_id", "type": "bigint"}, {"name": "partner_created_date", "type": "bigint"}, {"name": "funds_available_date", "type": "bigint"}, {"name": "funding_account", "type": "character varying"}, {"name": "method", "type": "character varying"}, {"name": "object", "type": "character varying"}, {"name": "partner_environment_mode", "type": "character varying"}, {"name": "related_original_settlement", "type": "character varying"}, {"name": "related_reversed_by_settlement", "type": "character varying"}, {"name": "related_settlement_exception_transaction", "type": "character varying"}, {"name": "settlement_exception_code", "type": "character varying"}, {"name": "source_original_settlement", "type": "character varying"}, {"name": "source_reversed_by_settlement", "type": "character varying"}, {"name": "source_settlement_exception_transaction", "type": "character varying"}, {"name": "source_transaction_id", "type": "character varying"}, {"name": "statement_narrative", "type": "character varying"}, {"name": "status", "type": "character varying"}, {"name": "transaction_id", "type": "character varying"}, {"name": "id", "type": "character varying"}, {"name": "string_partner_created_date", "type": "character varying"}, {"name": "account_id", "type": "character varying"}, {"name": "live_connection", "type": "character varying"}, {"name": "partner_source", "type": "character varying"}, {"name": "record_state", "type": "character varying"}, {"name": "source_id", "type": "character varying"}, {"name": "currency", "type": "character varying"}], "relationships": []}}                  question:         give me top 10 settlemnt by value     ');



