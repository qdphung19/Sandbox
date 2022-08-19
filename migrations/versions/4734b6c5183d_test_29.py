"""test 29

Revision ID: 4734b6c5183d
Revises: 7ec98f32aa4c
Create Date: 2022-08-19 15:40:42.703319

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4734b6c5183d'
down_revision = '7ec98f32aa4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('clients', 'client_nom',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('clients', 'client_prenom',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('clients', 'client_domain',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('clients', 'adresse',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    op.alter_column('clients', 'code_postal',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    op.alter_column('clients', 'ville',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    op.alter_column('clients', 'pays',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('employes', 'nom',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    op.alter_column('employes', 'prenom',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    op.alter_column('employes', 'date_de_naissance',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('employes', 'adresse',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    op.alter_column('enfances', 'nom',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('enfances', 'prenom',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('labos', 'labo_nom',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    op.alter_column('labos', 'responsable_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('processus', 'processus_nom',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('processus', 'processus_nom',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    op.alter_column('labos', 'responsable_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('labos', 'labo_nom',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    op.alter_column('enfances', 'prenom',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.alter_column('enfances', 'nom',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.alter_column('employes', 'adresse',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.alter_column('employes', 'date_de_naissance',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('employes', 'prenom',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    op.alter_column('employes', 'nom',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    op.alter_column('clients', 'pays',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.alter_column('clients', 'ville',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.alter_column('clients', 'code_postal',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.alter_column('clients', 'adresse',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.alter_column('clients', 'client_domain',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.alter_column('clients', 'client_prenom',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.alter_column('clients', 'client_nom',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    # ### end Alembic commands ###
