"""test 1

Revision ID: 9f591434275d
Revises: 
Create Date: 2022-08-17 15:03:13.388316

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9f591434275d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('employes', 'nom',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    op.alter_column('employes', 'prenom',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    op.alter_column('employes', 'date_de_naissance',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('employes', 'sex',
               existing_type=postgresql.ENUM('male', 'female', 'autre', name='sexenum'),
               nullable=False)
    op.alter_column('employes', 'adresse',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.drop_constraint('employes_surveillance_fkey', 'employes', type_='foreignkey')
    op.drop_column('employes', 'surveillance')
    op.alter_column('labos', 'labo_nom',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    op.alter_column('labos', 'date_deput',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.drop_constraint('labos_responsable_fkey', 'labos', type_='foreignkey')
    op.drop_column('labos', 'responsable')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('labos', sa.Column('responsable', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('labos_responsable_fkey', 'labos', 'employes', ['responsable'], ['employe_id'])
    op.alter_column('labos', 'date_deput',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('labos', 'labo_nom',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    op.add_column('employes', sa.Column('surveillance', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('employes_surveillance_fkey', 'employes', 'employes', ['surveillance'], ['employe_id'])
    op.alter_column('employes', 'adresse',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    op.alter_column('employes', 'sex',
               existing_type=postgresql.ENUM('male', 'female', 'autre', name='sexenum'),
               nullable=True)
    op.alter_column('employes', 'date_de_naissance',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('employes', 'prenom',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    op.alter_column('employes', 'nom',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    # ### end Alembic commands ###
