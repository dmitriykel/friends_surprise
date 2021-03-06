"""add user to authorization_codes

Revision ID: 891c0f4442ae
Revises: 0490bb73558d
Create Date: 2019-06-23 13:26:36.781105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '891c0f4442ae'
down_revision = '0490bb73558d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('authorization_codes', sa.Column('user', sa.String(length=16), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('authorization_codes', 'user')
    # ### end Alembic commands ###
