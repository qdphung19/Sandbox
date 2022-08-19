"""test 20

Revision ID: d57215464f8f
Revises: ff29456bed96
Create Date: 2022-08-19 10:56:01.257740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd57215464f8f'
down_revision = 'ff29456bed96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('enfances', sa.Column('sex', sa.Enum('male', 'female', 'autre', name='sexenum'), nullable=False))
    op.alter_column('labos', 'responsable_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('labos', 'responsable_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('enfances', 'sex')
    # ### end Alembic commands ###
