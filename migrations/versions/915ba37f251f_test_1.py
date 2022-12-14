"""test 1

Revision ID: 915ba37f251f
Revises: 8ef77bdfd769
Create Date: 2022-08-19 16:10:46.712058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '915ba37f251f'
down_revision = '8ef77bdfd769'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employes',
    sa.Column('employe_id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=32), nullable=True),
    sa.Column('prenom', sa.String(length=32), nullable=True),
    sa.Column('date_de_naissance', sa.DateTime(), nullable=True),
    sa.Column('sex', sa.Enum('Male', 'Female', 'Autre', name='sexenumemployes'), nullable=True),
    sa.Column('adresse', sa.String(length=128), nullable=True),
    sa.Column('salaire', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('employe_id')
    )
    op.create_table('labos',
    sa.Column('labo_id', sa.Integer(), nullable=False),
    sa.Column('labo_nom', sa.String(length=32), nullable=True),
    sa.Column('labo_adresse', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('labo_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('labos')
    op.drop_table('employes')
    # ### end Alembic commands ###
