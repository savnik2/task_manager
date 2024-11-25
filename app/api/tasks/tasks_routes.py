from fastapi import APIRouter, Depends
from app.api.dependencie import CurrentUser
from app.schemas.tasks import CreateTask
from app.services.task_service import TaskService

router = APIRouter(

    tags={'tasks'},
    prefix='/tasks',
)


@router.post('/create',
             summary='Создание задачи')
async def create_project(user: CurrentUser,
                         project_data: CreateTask,
                         task_service: TaskService = Depends(),
                         ):
    return await task_service.create_task(
        user.id,
        project_data,
    )


@router.post('/archived-task/{task_id}',
             summary='Задача в архиве')
async def archived_task(user: CurrentUser,
                        task_id: int,
                        status: str,
                        task_service: TaskService = Depends(),
                        ):
    return await task_service.archived_task(
        task_id,
        status,
    )
