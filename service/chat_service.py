# from fastapi import Depends
from snowflake.connector import SnowflakeConnection

from models.QueryResponse import Response
from utils.ai_utils import getAIResponse, parseResponse, getAISummery, get_llm_bedrock
from utils.db_utils import get_connection, runQuery, runPostgresQuery, runSnowfakeQuery
from utils.prompt import getFormattedPrompt


def getResponse(question: str, conn: SnowflakeConnection = get_connection()):
    query_response = getAIResponse(conn, getFormattedPrompt(question= question, type="QUERY_PROMPT"))
    # query_response = get_llm_bedrock(getFormattedPrompt(question= question, type="QUERY_PROMPT"))
    print("query response is ", query_response)
    parsedQueryResponse = parseResponse(query_response)
    print("generated query :", parsedQueryResponse.snowflakeQuery)
    # query_results = runQuery(conn, parsedQueryResponse)
    # query_results = runPostgresQuery(parsedQueryResponse.snowflakeQuery)
    query_results = runSnowfakeQuery(parsedQueryResponse.snowflakeQuery)
    print(query_results)

    if parsedQueryResponse.chartType == "text":
        query_results = getAISummery(conn, getFormattedPrompt(question=question, type="SUMMARY_PROMPT", response=query_results))
        print(query_results)

        # print("++++++++++++++++++++++++++++++")
        # print(getFormattedPrompt(question=question, type="SUMMARY_PROMPT", response=query_results))
        # print("++++++++++++++++++++++++++++++")
        #
        # query_results = get_llm_bedrock(getFormattedPrompt(question=question, type="SUMMARY_PROMPT", response=query_results))
    return Response(snowflakeQuery=parsedQueryResponse.snowflakeQuery,
                    chartType=parsedQueryResponse.chartType,
                    userQuestion=parsedQueryResponse.userQuestion,
                    response=query_results,
                    genericResponse=parsedQueryResponse.genericResponse,
                    genericResponseIdentifier=parsedQueryResponse.genericResponseIdentifier)



