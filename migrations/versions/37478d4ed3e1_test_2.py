"""test 2

Revision ID: 37478d4ed3e1
Revises: 386a08a9cfdd
Create Date: 2022-08-19 16:14:40.522610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37478d4ed3e1'
down_revision = '386a08a9cfdd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('enfances',
    sa.Column('enfance_id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=64), nullable=True),
    sa.Column('prenom', sa.String(length=64), nullable=True),
    sa.Column('date_de_naissance', sa.DateTime(), nullable=True),
    sa.Column('sex', sa.Enum('Male', 'Female', 'Autre', name='enumsexenfances'), nullable=True),
    sa.PrimaryKeyConstraint('enfance_id')
    )
    op.create_table('processus',
    sa.Column('processus_id', sa.Integer(), nullable=False),
    sa.Column('processus_nom', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('processus_id')
    )
    op.create_table('clients',
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('client_nom', sa.String(length=64), nullable=True),
    sa.Column('client_prenom', sa.String(length=64), nullable=True),
    sa.Column('client_domain', sa.String(length=64), nullable=True),
    sa.Column('adresse', sa.String(length=128), nullable=True),
    sa.Column('code_postal', sa.String(length=128), nullable=True),
    sa.Column('ville', sa.String(length=128), nullable=True),
    sa.Column('pays', sa.String(length=64), nullable=True),
    sa.Column('labo_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['labo_id'], ['labos.labo_id'], ),
    sa.PrimaryKeyConstraint('client_id'),
    sa.UniqueConstraint('client_domain')
    )
    op.create_table('employes_enfances',
    sa.Column('employe_id', sa.Integer(), nullable=False),
    sa.Column('enfance_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['employe_id'], ['employes.employe_id'], ),
    sa.ForeignKeyConstraint(['enfance_id'], ['enfances.enfance_id'], ),
    sa.PrimaryKeyConstraint('employe_id', 'enfance_id')
    )
    op.create_table('employes_processus',
    sa.Column('employe_id', sa.Integer(), nullable=False),
    sa.Column('processus_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['employe_id'], ['employes.employe_id'], ),
    sa.ForeignKeyConstraint(['processus_id'], ['processus.processus_id'], ),
    sa.PrimaryKeyConstraint('employe_id', 'processus_id')
    )
    op.create_table('point_collectes',
    sa.Column('point_collecte_id', sa.Integer(), nullable=False),
    sa.Column('point_collecte_nom', sa.String(length=128), nullable=True),
    sa.Column('point_collecte_adresse', sa.String(length=128), nullable=True),
    sa.Column('labo_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['labo_id'], ['labos.labo_id'], ),
    sa.PrimaryKeyConstraint('point_collecte_id')
    )
    op.add_column('employes', sa.Column('labo_id', sa.Integer(), nullable=True))
    op.add_column('employes', sa.Column('surveille_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'employes', 'employes', ['surveille_id'], ['employe_id'])
    op.create_foreign_key(None, 'employes', 'labos', ['labo_id'], ['labo_id'])
    op.add_column('labos', sa.Column('responsable_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'labos', 'employes', ['responsable_id'], ['employe_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'labos', type_='foreignkey')
    op.drop_column('labos', 'responsable_id')
    op.drop_constraint(None, 'employes', type_='foreignkey')
    op.drop_constraint(None, 'employes', type_='foreignkey')
    op.drop_column('employes', 'surveille_id')
    op.drop_column('employes', 'labo_id')
    op.drop_table('point_collectes')
    op.drop_table('employes_processus')
    op.drop_table('employes_enfances')
    op.drop_table('clients')
    op.drop_table('processus')
    op.drop_table('enfances')
    # ### end Alembic commands ###
