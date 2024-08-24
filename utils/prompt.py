import json
from typing import get_type_hints

from models.QueryResponse import QueryResponse

supported_visualization_chart = ["bar_chart", "pie_chart", "line_chart", "histogram", "text", "area_chart"]
context = {
    # "settlement_summary_daily": {
    #     "columns": [
    #         {
    #             "name": "id",
    #             "type": "bigint",
    #             "description": "Unique identifier for each daily settlement summary record"
    #         },
    #         {
    #             "name": "partner_source_id",
    #             "type": "integer",
    #             "description": "Identifier for the partner source (e.g., 4 for WORLDPAY, 6 for GLOBALPAYMENT, 2 for STRIPE)"
    #         },
    #         {
    #             "name": "date",
    #             "type": "date",
    #             "description": "The date of the settlement summary"
    #         },
    #         {
    #             "name": "month",
    #             "type": "integer",
    #             "description": "The month of the settlement summary (1-12)"
    #         },
    #         {
    #             "name": "year",
    #             "type": "integer",
    #             "description": "The year of the settlement summary"
    #         },
    #         {
    #             "name": "sum_settlement",
    #             "type": "numeric",
    #             "description": "The total amount settled for the day"
    #         },
    #         {
    #             "name": "count_settlement",
    #             "type": "integer",
    #             "description": "The number of settlements processed for the day"
    #         },
    #         {
    #             "name": "ledger_account_id",
    #             "type": "character varying",
    #             "description": "Identifier for the associated ledger account"
    #         },
    #         {
    #             "name": "institution_account_id",
    #             "type": "character varying",
    #             "description": "Identifier for the associated bank institution account"
    #         },
    #         {
    #             "name": "partner_account_id",
    #             "type": "character varying",
    #             "description": "Identifier for the partner's account"
    #         },
    #         {
    #             "name": "partner_source",
    #             "type": "character varying",
    #             "description": "Name of the partner source (e.g., WORLDPAY, GLOBALPAYMENT, STRIPE)"
    #         },
    #         {
    #             "name": "live_connection",
    #             "type": "character varying",
    #             "description": "Indicates if this is a live connection or test/sandbox environment"
    #         },
    #         {
    #             "name": "sum_settlement_currency",
    #             "type": "character varying",
    #             "description": "The currency of the settled amount"
    #         }
    #     ],
    #     "relationships": [],
    #     "description": "This table has settlement summary at a daily aggregation level"
    # },
    # "settlement_summary_monthly": {
    #     "columns": [
    #         {
    #             "name": "id",
    #             "type": "bigint",
    #             "description": "Unique identifier for each monthly settlement summary record"
    #         },
    #         {
    #             "name": "partner_source_id",
    #             "type": "integer",
    #             "description": "Identifier for the partner source (e.g., 4 for WORLDPAY, 6 for GLOBALPAYMENT, 2 for STRIPE)"
    #         },
    #         {
    #             "name": "month",
    #             "type": "integer",
    #             "description": "The month of the settlement summary (1-12)"
    #         },
    #         {
    #             "name": "year",
    #             "type": "integer",
    #             "description": "The year of the settlement summary"
    #         },
    #         {
    #             "name": "sum_settlement",
    #             "type": "numeric",
    #             "description": "The total amount settled for the month"
    #         },
    #         {
    #             "name": "count_settlement",
    #             "type": "integer",
    #             "description": "The number of settlements processed for the month"
    #         },
    #         {
    #             "name": "live_connection",
    #             "type": "character varying",
    #             "description": "Indicates if this is a live connection or test/sandbox environment"
    #         },
    #         {
    #             "name": "ledger_account_id",
    #             "type": "character varying",
    #             "description": "Identifier for the associated ledger account"
    #         },
    #         {
    #             "name": "institution_account_id",
    #             "type": "character varying",
    #             "description": "Identifier for the associated bank institution account"
    #         },
    #         {
    #             "name": "partner_account_id",
    #             "type": "character varying",
    #             "description": "Identifier for the partner's account"
    #         },
    #         {
    #             "name": "partner_source",
    #             "type": "character varying",
    #             "description": "Name of the partner source (e.g., WORLDPAY, GLOBALPAYMENT, STRIPE)"
    #         },
    #         {
    #             "name": "sum_settlement_currency",
    #             "type": "character varying",
    #             "description": "The currency of the settled amount"
    #         }
    #     ],
    #     "relationships": [],
    #     "description": "This table has settlement summary at a monthly aggregation level"
    # },
    # "settlement_summary_yearly": {
    #     "columns": [
    #         {
    #             "name": "id",
    #             "type": "bigint",
    #             "description": "Unique identifier for each yearly settlement summary record"
    #         },
    #         {
    #             "name": "partner_source_id",
    #             "type": "integer",
    #             "description": "Identifier for the partner source (e.g., 4 for WORLDPAY, 6 for GLOBALPAYMENT, 2 for STRIPE)"
    #         },
    #         {
    #             "name": "year",
    #             "type": "integer",
    #             "description": "The year of the settlement summary"
    #         },
    #         {
    #             "name": "sum_settlement",
    #             "type": "numeric",
    #             "description": "The total amount settled for the year"
    #         },
    #         {
    #             "name": "count_settlement",
    #             "type": "integer",
    #             "description": "The number of settlements processed for the year"
    #         },
    #         {
    #             "name": "live_connection",
    #             "type": "character varying",
    #             "description": "Indicates if this is a live connection or test/sandbox environment"
    #         },
    #         {
    #             "name": "sum_settlement_currency",
    #             "type": "character varying",
    #             "description": "The currency of the settled amount"
    #         },
    #         {
    #             "name": "ledger_account_id",
    #             "type": "character varying",
    #             "description": "Identifier for the associated ledger account"
    #         },
    #         {
    #             "name": "institution_account_id",
    #             "type": "character varying",
    #             "description": "Identifier for the associated bank institution account"
    #         },
    #         {
    #             "name": "partner_account_id",
    #             "type": "character varying",
    #             "description": "Identifier for the partner's account"
    #         },
    #         {
    #             "name": "partner_source",
    #             "type": "character varying",
    #             "description": "Name of the partner source (e.g., WORLDPAY, GLOBALPAYMENT, STRIPE)"
    #         }
    #     ],
    #     "relationships": [],
    #     "description": "This table has settlement summary at a yearly aggregation level"
    # },
    "ledger_account_relation_settlement": {
        "columns": [
            {
                "name": "ledger_account_id",
                "type": "character varying",
                "description": "Identifier for the ledger account"
            },
            {
                "name": "settlement_id",
                "type": "character varying",
                "description": "Identifier for the associated settlement"
            }
        ],
        "relationships": [
            {
                "column": "settlement_id",
                "foreign_table": "settlement",
                "foreign_column": "id"
            },
            {
                "column": "ledger_account_id",
                "foreign_table": "ledger_account_settlement",
                "foreign_column": "id"
            }
        ],
        "description": "This table is a relationship table between ledger_account_id and settlement_id"
    },
    "settlement": {
        "columns": [
            {
                "name": "amount",
                "type": "numeric",
                "description": "The amount of the settlement"
            },
            {
                "name": "modified_date",
                "type": "bigint",
                "description": "Timestamp of when the settlement was last modified"
            },
            {
                "name": "scheduled",
                "type": "boolean",
                "description": "Indicates if the settlement was scheduled"
            },
            {
                "name": "partner_account_connection_id",
                "type": "bigint",
                "description": "Identifier for the partner account connection"
            },
            {
                "name": "partner_source_id",
                "type": "bigint",
                "description": "Identifier for the partner source (e.g., 4 for WORLDPAY, 6 for GLOBALPAYMENT, 2 for STRIPE)"
            },
            {
                "name": "partner_created_date",
                "type": "bigint",
                "description": "Timestamp of when the settlement was created by the partner use it for all the "
                               "settlement info based on date"
            },
            {
                "name": "funds_available_date",
                "type": "bigint",
                "description": "Timestamp of when the funds will be available"
            },
            {
                "name": "funding_account",
                "type": "character varying",
                "description": "The account used for funding the settlement"
            },
            {
                "name": "method",
                "type": "character varying",
                "description": "The method used for settlement (e.g., ACH, wire transfer)"
            },
            {
                "name": "object",
                "type": "character varying",
                "description": "The type of object this settlement represents"
            },
            {
                "name": "partner_environment_mode",
                "type": "character varying",
                "description": "Indicates if this is a LIVE or TEST environment for the partner"
            },
            {
                "name": "related_original_settlement",
                "type": "character varying",
                "description": "Reference to the original settlement if this is a related transaction"
            },
            {
                "name": "related_reversed_by_settlement",
                "type": "character varying",
                "description": "Reference to the settlement that reversed this one, if applicable"
            },
            {
                "name": "related_settlement_exception_transaction",
                "type": "character varying",
                "description": "Reference to any exception transaction related to this settlement"
            },
            {
                "name": "settlement_exception_code",
                "type": "character varying",
                "description": "Code indicating any exception that occurred during settlement"
            },
            {
                "name": "source_original_settlement",
                "type": "character varying",
                "description": "Source of the original settlement if this is a related transaction"
            },
            {
                "name": "source_reversed_by_settlement",
                "type": "character varying",
                "description": "Source of the settlement that reversed this one, if applicable"
            },
            {
                "name": "source_settlement_exception_transaction",
                "type": "character varying",
                "description": "Source of any exception transaction related to this settlement"
            },
            {
                "name": "source_transaction_id",
                "type": "character varying",
                "description": "Identifier for the source transaction"
            },
            {
                "name": "statement_narrative",
                "type": "character varying",
                "description": "Narrative description of the settlement for statements"
            },
            {
                "name": "status",
                "type": "character varying",
                "description": "Current status of the settlement (e.g., pending, completed, failed)"
            },
            {
                "name": "transaction_id",
                "type": "character varying",
                "description": "Unique identifier for the transaction"
            },
            {
                "name": "id",
                "type": "character varying",
                "description": "Unique identifier for the settlement"
            },
            {
                "name": "string_partner_created_date",
                "type": "character varying",
                "description": "String representation of the settlement"
            },
            {
                "name": "account_id",
                "type": "character varying",
                "description": "Identifier for the account associated with this settlement"
            },
            {
                "name": "live_connection",
                "type": "character varying",
                "description": "Indicates if this is a live connection or TEST/LIVE environment"
            },
            {
                "name": "partner_source",
                "type": "character varying",
                "description": "Name of the partner source (e.g., WORLDPAY, GLOBALPAYMENT, STRIPE)"
            },
            {
                "name": "record_state",
                "type": "character varying",
                "description": "The current state of this record (e.g., active, archived)"
            },
            {
                "name": "source_id",
                "type": "character varying",
                "description": "unique Identifier for deduplication"
            },
            {
                "name": "currency",
                "type": "character varying",
                "description": "The currency of the settlement amount"
            }
        ],
        "relationships": [],
        "description": "This table has detailed settlement data"
    }
}

with open("./sf_scema.json", "r") as schema:
    schema = json.load(schema)

cot_template = """
        You are a Senior SnowSQL Developer working with a postgres Data Warehouse. 
        Instructions:
        - Break down the user query into smaller, more manageable steps. Follow the reasoning instructions steps below.
        - Use relevant columns from the context given below to filter and subset the data for each step.
        - Plan the final SnowSQL query based on the user's intent.
        - After planned the postgres sql query and based on the user query, decide which visualization chart will be
        more suitable to represent the output of the snow sql query. Choose from the supported visualization charts
        given below. Pick the chart from below list only as it is and send back the output.
        - Pick the colums from the given context below only. Dont construct the query with the attributes that's not 
        provided in the context. Context information is something you need to understand, then analyze the context 
        information with the user query and then plan, build the snow_sql query.
        - Follow the output parser format as a json only. The result should be returned in the specified format only. 
        Check the below sample query examples how user needs the output.
        - ledger_account_id is the unique id for each ledger.
        - return the query as per chart type so that i can plot the chart.
        - (((If the user query is not related to the context given below or don't have information of tables , you can 
            return a generic response and identifier also)))
        - give alias for each variable
        - make sure the column what you are adding to select statement belongs to specific table what we are using
        - always return the correct visualization charts type based on generated query and response because as per this 
        the data will be rendered in ui.
        
        
        output parser format:
        {}
        
        supported visualization charts:
        {}
        
        context:
        {}
        
        question:
        {}
    """

cot_template1 ="""You are a Senior SnowSQL Developer working with a Snowflake Data Warehouse. Your task is to convert natural language queries into SnowSQL queries and suggest appropriate visualizations. Use the following Chain-of-Thought process to approach each query:

1. Query Understanding:
   Thought: Carefully read and analyze the user's query. What is the main objective? What data elements are they interested in?
   Action: Summarize the key points of the user's request.

2. Context Analysis:
   Thought: Examine the provided context information. Which tables and columns are relevant to the user's query?
   Action: List the relevant tables and columns from the context.

3. Query Breakdown:
   Thought: How can we break down this query into smaller, more manageable steps?
   Action: Outline the steps needed to answer the query, considering necessary data manipulations.

4. SQL Planning:
   Thought: What SQL operations will be required for each step? Consider JOINs, WHERE clauses, aggregations, etc.
   Action: Sketch out the basic structure of the SQL query, including main clauses and operations.

5. Column and Table Verification:
   Thought: Are we only using columns and tables mentioned in the context? Do we need to create any aliases?
   Action: Verify and list the final set of columns and tables to be used, including any necessary aliases.

6. Query Construction:
   Thought: How do we put all the pieces together to form the final SnowSQL query?
   Action: Write the complete SnowSQL query, ensuring it follows Snowflake best practices and uses ledger_account_id as the unique identifier where appropriate.

7. Visualization Selection:
   Thought: Based on the query output, which visualization from the supported list would best represent the data?
   Action: Choose and justify the most appropriate visualization chart.

8. Output Formatting:
   Thought: How should we format the final output to match the required parser format?
   Action: Structure the response according to the specified output parser format.

9. Final Verification:
   Thought: Does our query and visualization fully address the user's request? Are there any potential issues or improvements?
   Action: Perform a final check and make any necessary adjustments.

Important Notes:
- Use only tables and columns mentioned in the provided context.
- If the user query is unrelated to the given context or lacks necessary table information, provide a generic response and identifier.
- Always provide an alias for each variable in the query.
- Ensure that columns in the SELECT statement belong to the tables being used.
- Choose the visualization chart from the supported list only.

Output Parser Format:
{}

Supported Visualization Charts:
{}

Context:
{}

User Query:
{}

For each step in your Chain-of-Thought process, clearly state your thought process and the resulting action. This will provide a transparent reasoning path from the initial query to the final SnowSQL query and visualization choice.
"""


summery_prompt = """
You are an assistant. Your task is to provide a pinpoint humanized response based on the user question and the 
provided response. Ensure the response is easy to understand and do not add extra content try to give precise answer 
based on question.

Question: {}

Response: {}
"""

cot_template_sf = """
    You are a Senior SnowSQL Developer working with a Snowflake Data Warehouse. 
    Instructions:
    - Break down the user query into smaller, more manageable steps. Follow the reasoning instructions steps below.
    - Use relevant columns from the context given below to filter and subset the data for each step.
    - Plan the final SnowSQL query based on the user's intent.
    - After planning the SnowSQL query and based on the user query, decide which visualization chart will be
      more suitable to represent the output of the SnowSQL query. Choose from the supported visualization charts
      given below. Pick the chart from the list only as it is and send back the output.
    - Pick the columns from the given context below only. Don’t construct the query with attributes that are not 
      provided in the context. Context information is something you need to understand, then analyze the context 
      information with the user query and then plan, build the SnowSQL query.
    - Follow the output parser format as JSON only. The result should be returned in the specified format only. 
      Check the below sample query examples of how users need the output.
    - Use aliases for each variable.
    - Make sure the column you are adding to the SELECT statement belongs to the specific table you are using.
    - Always return the correct visualization chart type based on the generated query and response, as this 
      determines how the data will be rendered in the UI, if the question is related to distribution chose pie chart if relevant.
    - when extracting month it should be jan, feb, mar, apr, may..
    - use these enums for financial_metric -  Balance,Credit Score,Income,Expenditure
    - if the question is related to the given context schema then its not an generic answer so fill the generic identifier carefully
    
      
      
    example -
    1.  
    question - How many payments were made each month?
    query - "SELECT 
    TO_CHAR(payment_date, 'Mon') AS payment_month,
    COUNT(payment_id) AS num_payments
    FROM payments
    GROUP BY payment_month
    ORDER BY MIN(payment_date);"

    Output parser format:
    {}

    Supported visualization charts:
    {}

    Context:
    {}

    Question:
    {}
"""


def getFormattedPrompt(**kwargs):
    if kwargs.get("type") == "QUERY_PROMPT":
        return cot_template_sf.format(get_type_hints(QueryResponse), supported_visualization_chart,
                                   schema, kwargs.get("question", ""))
    elif kwargs.get("type") == "SUMMARY_PROMPT":
        return summery_prompt.format(kwargs.get("question", ""), kwargs.get("response", ""))


# print(getFormattedPrompt(question= "ques", type="QUERY_PROMPT"))