from typing import Optional

from pydantic import BaseModel
from datetime import date, time


class CreateTask(BaseModel):
    name: str
    time: time
    date: date
    deadline: Optional[date]
    status: str
