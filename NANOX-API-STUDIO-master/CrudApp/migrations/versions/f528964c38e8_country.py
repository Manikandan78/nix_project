"""country

Revision ID: f528964c38e8
Revises: 6e86c994df0b
Create Date: 2024-06-13 12:43:04.796095

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f528964c38e8'
down_revision: Union[str, None] = '6e86c994df0b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('country', sa.Column('demo6', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('country', 'demo6')
    # ### end Alembic commands ###
