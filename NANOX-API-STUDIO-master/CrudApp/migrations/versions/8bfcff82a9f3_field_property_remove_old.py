"""field_property_remove_old

Revision ID: 8bfcff82a9f3
Revises: 499a0e9f87bc
Create Date: 2024-03-16 16:07:18.984256

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8bfcff82a9f3'
down_revision: Union[str, None] = '499a0e9f87bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('api_fields', 'old_field_property')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('api_fields', sa.Column('old_field_property', sa.TEXT(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
