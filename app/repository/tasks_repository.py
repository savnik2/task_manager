from app.models.users import Tasks
from app.repository.base import SQLAlchemyRepository


class TasksRepository(SQLAlchemyRepository):
    model = Tasks
