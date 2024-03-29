from repository.base import SQLAlchemyRepository
from models.users import Users
from database.session import DBSession
class UserRepository(SQLAlchemyRepository):
    model = Users


