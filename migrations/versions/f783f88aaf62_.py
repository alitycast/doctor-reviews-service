"""empty message

Revision ID: f783f88aaf62
Revises: 9eddc73049c8
Create Date: 2018-05-03 14:39:10.213495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f783f88aaf62'
down_revision = '9eddc73049c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'active')
    # ### end Alembic commands ###