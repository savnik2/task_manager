from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import force_auto_coercion
from app.models.base import Base
from datetime import time, date

force_auto_coercion()


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)

    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]

    projects: Mapped['Projects'] = relationship(back_populates='user')
    task: Mapped['Tasks'] = relationship(back_populates='user')


class Projects(Base):
    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), index=True)

    user: Mapped['Users'] = relationship(back_populates='projects')
    task: Mapped['Tasks'] = relationship(back_populates='project')

class Tasks(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    project_id: Mapped[int] = mapped_column(ForeignKey('projects.id'), index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), index=True)
    name: Mapped[str]
    time: Mapped[time]
    date: Mapped[date]
    deadline: Mapped[date | None]
    status: Mapped[str] = mapped_column(server_default="Второстепенная")

    user: Mapped['Users'] = relationship(back_populates='task')
    project: Mapped['Projects'] = relationship(back_populates='task')

    

class TasksArchive(Base):
    __tablename__ = 'tasks_archive'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    project_id: Mapped[int] = mapped_column(ForeignKey('projects.id'), index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), index=True)
    name: Mapped[str]
    archived_date: Mapped[date]
    status: Mapped[str]


