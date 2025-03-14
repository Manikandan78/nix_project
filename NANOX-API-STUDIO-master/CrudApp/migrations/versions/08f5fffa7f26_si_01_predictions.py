"""si_01_predictions

Revision ID: 08f5fffa7f26
Revises: ab048bb6f7af
Create Date: 2024-07-12 15:35:25.067633

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08f5fffa7f26'
down_revision: Union[str, None] = 'ab048bb6f7af'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('si_01_predictions', sa.Column('character', sa.Float(), nullable=True))
    op.add_column('si_01_predictions', sa.Column('advertise_mediums', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('si_01_predictions', 'advertise_mediums')
    op.drop_column('si_01_predictions', 'character')
    # ### end Alembic commands ###
