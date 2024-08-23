from dataclasses import dataclass
from typing import List, get_type_hints


@dataclass
class QueryResponse:
    snowflakeQuery: str
    chartType: str
    userQuestion: str
    genericResponseIdentifier: bool
    genericResponse: str

@dataclass
class Response(QueryResponse):
    response: str | List[str]

