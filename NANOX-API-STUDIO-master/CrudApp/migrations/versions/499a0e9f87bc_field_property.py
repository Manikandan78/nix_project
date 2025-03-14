"""field_property

Revision ID: 499a0e9f87bc
Revises: 359eb44ce07d
Create Date: 2024-03-16 16:04:21.835307

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '499a0e9f87bc'
down_revision: Union[str, None] = '359eb44ce07d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('api_cms_page_migrations', 'created_date')
    op.add_column('api_fields', sa.Column('field_property', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('api_fields', 'field_property')
    op.add_column('api_cms_page_migrations', sa.Column('created_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
