from app.models.users import Projects
from app.repository.base import SQLAlchemyRepository


class ProjectRepository(SQLAlchemyRepository):
    model = Projects