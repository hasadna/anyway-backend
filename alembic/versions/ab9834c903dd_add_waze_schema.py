"""Add waze schema

Revision ID: ab9834c903dd
Revises: f4213b13820d
Create Date: 2020-03-24 22:21:04.780038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab9834c903dd'
down_revision = 'f4213b13820d'
branch_labels = None
depends_on = None

schemas_names = ['waze']

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    for schema_name in schemas_names:
        cmd = "CREATE SCHEMA IF NOT EXISTS " + schema_name
        op.execute(cmd)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    for schema_name in schemas_names:
        cmd = "DROP SCHEMA IF EXISTS " + schema_name
        op.execute(cmd)
    # ### end Alembic commands ###
