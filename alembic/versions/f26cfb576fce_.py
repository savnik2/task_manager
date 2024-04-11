"""empty message

Revision ID: f26cfb576fce
Revises: 9b3b3f8246b0
Create Date: 2024-04-11 11:47:34.103051

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f26cfb576fce'
down_revision = '9b3b3f8246b0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_tasks_id', table_name='tasks')
    op.drop_index('ix_tasks_project_id', table_name='tasks')
    op.drop_index('ix_tasks_user_id', table_name='tasks')
    op.drop_table('tasks')
    op.drop_index('ix_projects_id', table_name='projects')
    op.drop_index('ix_projects_user_id', table_name='projects')
    op.drop_table('projects')
    op.drop_index('ix_users_id', table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('users_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email', name='users_email_key'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    op.create_table('projects',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('projects_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='projects_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='projects_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_projects_user_id', 'projects', ['user_id'], unique=False)
    op.create_index('ix_projects_id', 'projects', ['id'], unique=False)
    op.create_table('tasks',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('project_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('time', postgresql.TIME(), autoincrement=False, nullable=False),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('deadline', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(), server_default=sa.text("'Второстепенная'::character varying"), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], name='tasks_project_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='tasks_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='tasks_pkey')
    )
    op.create_index('ix_tasks_user_id', 'tasks', ['user_id'], unique=False)
    op.create_index('ix_tasks_project_id', 'tasks', ['project_id'], unique=False)
    op.create_index('ix_tasks_id', 'tasks', ['id'], unique=False)
    # ### end Alembic commands ###
