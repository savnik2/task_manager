from pydantic import BaseModel


class CreateGroup(BaseModel):
    admin_id: int
    project_id: int
