"""empty message

Revision ID: 4626e0b45a8f
Revises: f9ff36b488b4
Create Date: 2022-08-12 22:55:55.760089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4626e0b45a8f'
down_revision = 'f9ff36b488b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_venues', sa.String(length=500), nullable=True))
    op.drop_column('Artist', 'seeking_description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_description', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
    op.drop_column('Artist', 'seeking_venues')
    # ### end Alembic commands ###
