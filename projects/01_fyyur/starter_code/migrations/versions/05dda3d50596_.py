"""empty message

Revision ID: 05dda3d50596
Revises: cf6609a0181a
Create Date: 2022-08-11 23:01:13.072197

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05dda3d50596'
down_revision = 'cf6609a0181a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('looking_for', sa.Boolean(), nullable=True))
    op.add_column('Artist', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'seeking_description')
    op.drop_column('Artist', 'looking_for')
    # ### end Alembic commands ###