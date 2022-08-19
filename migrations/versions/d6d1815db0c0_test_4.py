"""test 4

Revision ID: d6d1815db0c0
Revises: d71ee07c1e11
Create Date: 2022-08-17 17:27:37.047431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6d1815db0c0'
down_revision = 'd71ee07c1e11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employes', sa.Column('surveille_id', sa.Integer(), nullable=True))
    op.drop_constraint('employes_surveille_par_fkey', 'employes', type_='foreignkey')
    op.create_foreign_key(None, 'employes', 'employes', ['surveille_id'], ['employe_id'])
    op.drop_column('employes', 'surveille_par')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employes', sa.Column('surveille_par', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'employes', type_='foreignkey')
    op.create_foreign_key('employes_surveille_par_fkey', 'employes', 'employes', ['surveille_par'], ['employe_id'])
    op.drop_column('employes', 'surveille_id')
    # ### end Alembic commands ###
