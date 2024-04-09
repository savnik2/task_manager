from fastapi import APIRouter, Depends
from app.api.dependencie import CurrentUser
from app.schemas.tasks import CreateTask
from app.services.task_service import TaskService

router = APIRouter(

    tags={'tasks'},

    prefix='/tasks',
)


@router.post('/create')
async def create_project(user: CurrentUser,
                         project_data: CreateTask,
                         project_service: TaskService = Depends(),
                         ):
    return await project_service.create_task(
        user.id,
        project_data,
    )

