"""asa0201_01_01

Revision ID: ccb820545fc6
Revises: b2d2875048ba
Create Date: 2024-04-03 16:17:12.362060

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ccb820545fc6'
down_revision: Union[str, None] = 'b2d2875048ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('asa0201_01_01', sa.Column('user_role', sa.String(), nullable=True))
    op.add_column('asa0201_01_01', sa.Column('user_role_privilege', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('asa0201_01_01', 'user_role_privilege')
    op.drop_column('asa0201_01_01', 'user_role')
    # ### end Alembic commands ###
