"""gift tables

Revision ID: 8e45e0dcb8f3
Revises: 0c0ff17efbf6
Create Date: 2019-06-18 12:39:59.707764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e45e0dcb8f3'
down_revision = '0c0ff17efbf6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gifts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gifts_books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gift_id', sa.Integer(), nullable=True),
    sa.Column('link', sa.String(length=140), nullable=True),
    sa.ForeignKeyConstraint(['gift_id'], ['gifts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gifts_games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gift_id', sa.Integer(), nullable=True),
    sa.Column('codes', sa.String(length=140), nullable=True),
    sa.ForeignKeyConstraint(['gift_id'], ['gifts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gifts_tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gift_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.String(length=140), nullable=True),
    sa.ForeignKeyConstraint(['gift_id'], ['gifts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gifts_types',
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('type_name', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['type_id'], ['gifts.type_id'], ),
    sa.PrimaryKeyConstraint('type_id')
    )
    op.drop_index('ix_surprises_released', table_name='surprises')
    op.drop_table('surprises')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('surprises',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('content', sa.VARCHAR(length=140), nullable=True),
    sa.Column('released', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_surprises_released', 'surprises', ['released'], unique=False)
    op.drop_table('gifts_types')
    op.drop_table('gifts_tasks')
    op.drop_table('gifts_games')
    op.drop_table('gifts_books')
    op.drop_table('gifts')
    # ### end Alembic commands ###