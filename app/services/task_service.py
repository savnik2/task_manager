from fastapi import Depends

from app.repository.tasks_repository import TasksRepository
from app.schemas.tasks import CreateTask, TaskInDB


class TaskService:

    def __init__(
            self,
            task_repo: TasksRepository = Depends(),
    ):
        self.task_repo = task_repo

    async def create_task(
            self,
            user_id: int,
            task_data: CreateTask
    ):
        task_data = TaskInDB(
            **task_data.model_dump(),
            user_id=user_id,
        )
        return await self.task_repo.create(task_data.model_dump())
