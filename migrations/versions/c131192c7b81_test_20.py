"""test 20

Revision ID: c131192c7b81
Revises: 1f86964149c3
Create Date: 2022-08-19 11:28:19.367570

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c131192c7b81'
down_revision = '1f86964149c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('enfances',
    sa.Column('enfance_id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=64), nullable=False),
    sa.Column('prenom', sa.String(length=64), nullable=False),
    sa.Column('date_de_naissance', sa.DateTime(), nullable=True),
    sa.Column('sex', postgresql.ENUM('Male', 'Female', 'Autre', name='sex_enfances'), nullable=False),
    sa.Column('parent_1_id', sa.Integer(), nullable=False),
    sa.Column('parent_2_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_1_id'], ['employes.employe_id'], ),
    sa.ForeignKeyConstraint(['parent_2_id'], ['employes.employe_id'], ),
    sa.PrimaryKeyConstraint('enfance_id')
    )
    op.alter_column('labos', 'responsable_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('labos', 'responsable_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_table('enfances')
    # ### end Alembic commands ###