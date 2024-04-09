from typing import Optional

from pydantic import BaseModel, Field
from datetime import date, time


class CreateTask(BaseModel):
    name: str
    time: time
    date: date
    deadline: Optional[date] = Field(default=None)
    status: str
    project_id: Optional[int] = Field(default=None)


class TaskInDB(CreateTask):
    user_id: int
