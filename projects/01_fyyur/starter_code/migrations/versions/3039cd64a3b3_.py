"""empty message

Revision ID: 3039cd64a3b3
Revises: 5ae4d397e169
Create Date: 2022-08-11 23:48:30.602436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3039cd64a3b3'
down_revision = '5ae4d397e169'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Shows',
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('venue_id', 'artist_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Shows')
    # ### end Alembic commands ###
