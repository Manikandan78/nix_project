"""MODEL LOG

Revision ID: fa1cf20c17f9
Revises: 42ddf6e9de60
Create Date: 2024-01-03 16:40:36.685754

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fa1cf20c17f9'
down_revision: Union[str, None] = '42ddf6e9de60'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api_model_logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('table_id', sa.Integer(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('log', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['table_id'], ['api_models.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_api_model_logs_id'), 'api_model_logs', ['id'], unique=False)
    op.add_column('api_models', sa.Column('cms_page', sa.Integer(), nullable=True))
    op.add_column('api_models', sa.Column('cms_uid', sa.String(), nullable=True))
    op.add_column('api_models', sa.Column('cms_api_name', sa.String(), nullable=True))
    op.add_column('api_models', sa.Column('cms_file_type', sa.String(), nullable=True))
    op.create_foreign_key(None, 'api_models', 'api_cms_page', ['cms_page'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'api_models', type_='foreignkey')
    op.drop_column('api_models', 'cms_file_type')
    op.drop_column('api_models', 'cms_api_name')
    op.drop_column('api_models', 'cms_uid')
    op.drop_column('api_models', 'cms_page')
    op.drop_index(op.f('ix_api_model_logs_id'), table_name='api_model_logs')
    op.drop_table('api_model_logs')
    # ### end Alembic commands ###
