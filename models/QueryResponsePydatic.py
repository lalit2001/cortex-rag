from pydantic import BaseModel
from typing import List, Union

class QueryResponse(BaseModel):
    snowflakeQuery: str
    chartType: str
    userQuestion: str
    genericResponseIdentifier: bool
    genericResponse: str

class Response(QueryResponse):
    response: Union[str, List[str]]