"""test 3

Revision ID: d71ee07c1e11
Revises: 16dce0a01d1c
Create Date: 2022-08-17 16:49:04.660427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd71ee07c1e11'
down_revision = '16dce0a01d1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('surveiller_table')
    op.add_column('employes', sa.Column('surveille_par', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'employes', 'employes', ['surveille_par'], ['employe_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'employes', type_='foreignkey')
    op.drop_column('employes', 'surveille_par')
    op.create_table('surveiller_table',
    sa.Column('qui_surveille_autre', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('qui_est_surveille', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['qui_est_surveille'], ['employes.employe_id'], name='surveiller_table_qui_est_surveille_fkey'),
    sa.ForeignKeyConstraint(['qui_surveille_autre'], ['employes.employe_id'], name='surveiller_table_qui_surveille_autre_fkey')
    )
    # ### end Alembic commands ###