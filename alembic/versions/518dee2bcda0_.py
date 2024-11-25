"""empty message

Revision ID: 518dee2bcda0
Revises: 651ae78051d9
Create Date: 2024-08-30 19:21:20.446955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '518dee2bcda0'
down_revision = '651ae78051d9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('groups_project_id_fkey', 'groups', type_='foreignkey')
    op.drop_column('groups', 'project_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('groups', sa.Column('project_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('groups_project_id_fkey', 'groups', 'projects', ['project_id'], ['id'])
    # ### end Alembic commands ###
