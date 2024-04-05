from pydantic import BaseModel


class CreateProject(BaseModel):
    name: str


class ProjectInDB(CreateProject):
    user_id: int
