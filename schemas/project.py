from pydantic import BaseModel
from datetime import date
# from enum import Enum
from models.project import Status, Express


# class ProjectStatus(str, Enum):
#     complete = "Complete"
#     incomplete = "Incomplete"


# class ProjectExpress(str, Enum):
#     true = "True"
#     false = "False"

class Project(BaseModel):
    # projectId: int
    title: str = ""
    userId: int
    clientId: int
    cutId: int
    description: str = ""
    # descImg: str
    fee: float = 0
    status: Status = 'Incomplete'
    isExpress: Express = 'False'
    due_date: date

    class Config:
        use_enum_values = True