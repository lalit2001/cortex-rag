import json
from llama_index.core.base.llms.types import MessageRole, ChatMessage
from llama_index.llms.bedrock import Bedrock
from snowflake.connector import SnowflakeConnection

from models.QueryResponse import QueryResponse
from utils.config import config


def getAIResponse(connection: SnowflakeConnection, prompt: str) -> str:
    cs = connection.cursor()
    val = ' '.join(prompt.splitlines()).replace("'", '"')

    try:
        cs.execute(
            f"SELECT SNOWFLAKE.CORTEX.COMPLETE('llama3.1-405b', '{val}');")
        one_row = cs.fetchone()
        return one_row[0]
    finally:
        cs.close()

def getAISummery(connection: SnowflakeConnection, prompt: str) -> str:
    cs = connection.cursor()
    print("==============================")
    val = ' '.join(prompt.splitlines()).replace("'", '"')
    print(f"SELECT SNOWFLAKE.CORTEX.COMPLETE('snowflake-arctic', '{val}');")
    print("==============================")
    try:
        cs.execute(
            f"SELECT SNOWFLAKE.CORTEX.COMPLETE('snowflake-arctic', '{val}');")
        one_row = cs.fetchone()
        print(one_row)
        return one_row[0]
    finally:
        print(one_row)
        cs.close()

def parseResponse(response: str) -> QueryResponse:
    start_pos = response.find('{')
    end_pos = response.rfind('}') + 1
    response = response[start_pos:end_pos]
    response = response.replace('\n', ' ')
    response = response.replace('True', 'true')
    response = response.replace('False', 'false')
    parsed_response = QueryResponse(**json.loads(response))
    return parsed_response


def get_llm_bedrock(messages, temperature=0.5):
    llm = Bedrock(model="anthropic.claude-3-5-sonnet-20240620-v1:0", max_tokens=20000, context_size=200000,
                  temperature=temperature,
                  aws_access_key_id=config.AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
                  region_name=config.AWS_SECRET_ACCESS_KEY)
    return llm.chat([ChatMessage(content=messages, role=MessageRole.USER)]).message.content

