"""api_sql

Revision ID: 5c7be9a5a2d3
Revises: 009030bf78fe
Create Date: 2024-03-13 17:14:45.774328

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5c7be9a5a2d3'
down_revision: Union[str, None] = '009030bf78fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api_sql',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.String(), nullable=True),
    sa.Column('psk_uid', sa.String(), nullable=True),
    sa.Column('api_name', sa.String(), nullable=True),
    sa.Column('api_type', sa.String(), nullable=True),
    sa.Column('api_method', sa.String(), nullable=True),
    sa.Column('db_connection', sa.Integer(), nullable=True),
    sa.Column('db_connection_name', sa.String(), nullable=True),
    sa.Column('api_schema', sa.String(), nullable=True),
    sa.Column('sql_text', sa.Text(), nullable=True),
    sa.Column('api_header_requests', sa.Text(), nullable=True),
    sa.Column('api_header', sa.Text(), nullable=True),
    sa.Column('api_header_property', sa.Text(), nullable=True),
    sa.Column('document_url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_api_sql_id'), 'api_sql', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_api_sql_id'), table_name='api_sql')
    op.drop_table('api_sql')
    # ### end Alembic commands ###
