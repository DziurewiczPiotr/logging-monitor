from pydantic import BaseModel


class Log(BaseModel):
    level: str
    message: str


class AppMeta(BaseModel):
    name: str
    version: str
    description: str
    authors: list[str]


class Logs(BaseModel):
    logs: list[Log]
