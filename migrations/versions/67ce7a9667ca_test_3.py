"""test 3

Revision ID: 67ce7a9667ca
Revises: 37478d4ed3e1
Create Date: 2022-08-19 17:12:15.326224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67ce7a9667ca'
down_revision = '37478d4ed3e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('processus', sa.Column('processus_description', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('processus', 'processus_description')
    # ### end Alembic commands ###
