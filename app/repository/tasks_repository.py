from app.models.models import Tasks, TasksArchive
from app.repository.base import SQLAlchemyRepository


class TasksRepository(SQLAlchemyRepository):
    model = Tasks


class TasksArchiveRepository(SQLAlchemyRepository):
    model = TasksArchive
