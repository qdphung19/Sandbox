"""test 7

Revision ID: a119de0b5f49
Revises: b42cd0722256
Create Date: 2022-08-18 12:00:10.559836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a119de0b5f49'
down_revision = 'b42cd0722256'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('employes_processus', 'employe_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('employes_processus', 'processus_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.add_column('labos', sa.Column('supervisor_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'labos', 'employes', ['supervisor_id'], ['employe_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'labos', type_='foreignkey')
    op.drop_column('labos', 'supervisor_id')
    op.alter_column('employes_processus', 'processus_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('employes_processus', 'employe_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
