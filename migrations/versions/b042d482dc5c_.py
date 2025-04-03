"""empty message

Revision ID: b042d482dc5c
Revises: 30692705010d
Create Date: 2024-07-31 21:43:39.166861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b042d482dc5c'
down_revision = '30692705010d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('acc_friends',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('friends', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('pk')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('acc_friends')
    # ### end Alembic commands ###
