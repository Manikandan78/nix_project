"""am

Revision ID: 524eef528b3a
Revises: 8233dbea564b
Create Date: 2024-09-10 16:03:16.783466

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '524eef528b3a'
down_revision: Union[str, None] = '8233dbea564b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('am', sa.Column('sample', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('am', 'sample')
    # ### end Alembic commands ###
