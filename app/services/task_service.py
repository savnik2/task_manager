from datetime import datetime

from fastapi import Depends

from app.repository.tasks_repository import TasksRepository, TasksArchiveRepository
from app.schemas.tasks import CreateTask, TaskInDB


class TaskService:

    def __init__(
            self,
            task_repo: TasksRepository = Depends(),
            archive_repo: TasksArchiveRepository = Depends(),
    ):
        self.task_repo = task_repo
        self.archive_repo = archive_repo

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

    async def archived_task(
            self,
            task_id,
            status,
    ):
        task = await self.task_repo.get(id=task_id)
        today = datetime.today()
        task_dict = {
            "project_id": task.project_id,
            "user_id": task.user_id,
            "name": task.name,
            "archived_date": today,
            "status": status,
        }
        archived_task = await self.archive_repo.create(task_dict)

        return archived_task

