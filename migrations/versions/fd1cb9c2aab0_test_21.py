"""test 21

Revision ID: fd1cb9c2aab0
Revises: c131192c7b81
Create Date: 2022-08-19 11:38:08.634798

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fd1cb9c2aab0'
down_revision = 'c131192c7b81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employes', sa.Column('sex', postgresql.ENUM('Male', 'Female', 'Autre', name='sex'), nullable=False))
    op.add_column('enfances', sa.Column('sex', postgresql.ENUM('Male', 'Female', 'Autre', name='sex'), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('enfances', 'sex')
    op.drop_column('employes', 'sex')
    # ### end Alembic commands ###
