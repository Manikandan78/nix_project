"""cmspageupdatefield

Revision ID: 9554d19453ba
Revises: 02c61a23fc78
Create Date: 2024-03-16 15:45:40.613075

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9554d19453ba'
down_revision: Union[str, None] = '02c61a23fc78'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('api_cms_page', sa.Column('api_code_name', sa.Text(), nullable=True))
    op.add_column('api_cms_page', sa.Column('api_code_file', sa.LargeBinary(), nullable=True))
    op.add_column('api_cms_page_migrations', sa.Column('api_code_name', sa.Text(), nullable=True))
    op.add_column('api_cms_page_migrations', sa.Column('api_code_file', sa.LargeBinary(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('api_cms_page_migrations', 'api_code_file')
    op.drop_column('api_cms_page_migrations', 'api_code_name')
    op.drop_column('api_cms_page', 'api_code_file')
    op.drop_column('api_cms_page', 'api_code_name')
    # ### end Alembic commands ###
