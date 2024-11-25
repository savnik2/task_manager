from sqlalchemy import ForeignKey, Table, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import force_auto_coercion
from app.models.base import Base
from datetime import time, date

force_auto_coercion()

user_group_association = Table(
    'user_group', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('group_id', Integer, ForeignKey('groups.id'))
)


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)

    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    name: Mapped[str]
    surname: Mapped[str]

    projects: Mapped['Projects'] = relationship(back_populates='owner')
    task: Mapped['Tasks'] = relationship(back_populates='user')
    groups: Mapped['Groups'] = relationship(secondary=user_group_association, back_populates='members')


class Groups(Base):
    __tablename__ = 'groups'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)

    admin_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    project_id: Mapped[int] = mapped_column(ForeignKey('projects.id'))
    project: Mapped['Projects'] = relationship(back_populates='group')

    members: Mapped['Users'] = relationship(secondary=user_group_association, back_populates='groups')


class Projects(Base):
    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str]

    owner_id: Mapped[int] = mapped_column(ForeignKey('users.id'), index=True)
    owner: Mapped['Users'] = relationship(back_populates='projects')

    task: Mapped['Tasks'] = relationship(back_populates='project')

    group: Mapped['Groups'] = relationship(back_populates='project')



class Tasks(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    project_id: Mapped[int] = mapped_column(ForeignKey('projects.id'), index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), index=True)
    name: Mapped[str]
    time: Mapped[time]
    date: Mapped[date]
    deadline: Mapped[date | None]
    status: Mapped[str] = mapped_column(server_default='Второстепенная')

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
