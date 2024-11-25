from fastapi import APIRouter, Depends

from app.api.dependencie import CurrentUser
from app.schemas.groups import CreateGroup
from app.services.group_service import GroupService

router = APIRouter(

    tags=['groups'],

    prefix='/groups',

)


@router.post('/create',
             summary='Создание групп')
async def create_group(user: CurrentUser,
                       group_data: CreateGroup,
                       group_service: GroupService = Depends(),
                       ):
    return await group_service.create_group(
        user.id,
        group_data,
    )
