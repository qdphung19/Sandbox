"""test 21

Revision ID: 077c64df3381
Revises: b1d3214448dc
Create Date: 2022-08-20 23:16:54.753111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '077c64df3381'
down_revision = 'b1d3214448dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('resultats',
    sa.Column('resultat_id', sa.Integer(), nullable=False),
    sa.Column('resultat_date', sa.DateTime(), nullable=False),
    sa.Column('degree', sa.Float(), nullable=True),
    sa.Column('glucose', sa.Float(), nullable=True),
    sa.Column('ph', sa.Float(), nullable=True),
    sa.Column('sample_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sample_id'], ['samples.sample_id'], ),
    sa.PrimaryKeyConstraint('resultat_id')
    )
    op.add_column('samples', sa.Column('sample_id', sa.Integer(), nullable=False))
    op.drop_column('samples', 'samples_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('samples', sa.Column('samples_id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_column('samples', 'sample_id')
    op.drop_table('resultats')
    # ### end Alembic commands ###
