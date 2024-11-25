from pydantic import BaseModel


class CreateProject(BaseModel):
    name: str


class ProjectInDB(CreateProject):
    owner_id: int
