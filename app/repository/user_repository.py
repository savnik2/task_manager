from app.repository.base import SQLAlchemyRepository
from app.models.users import Users, Projects, Tasks


class UserRepository(SQLAlchemyRepository):
    model = Users





