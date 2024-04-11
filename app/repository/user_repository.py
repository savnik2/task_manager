from app.repository.base import SQLAlchemyRepository
from app.models.models import Users


class UserRepository(SQLAlchemyRepository):
    model = Users
