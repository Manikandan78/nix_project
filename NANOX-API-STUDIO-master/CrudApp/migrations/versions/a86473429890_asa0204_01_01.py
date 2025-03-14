""""asa0204_01_01"

Revision ID: a86473429890
Revises: 3604a23214eb
Create Date: 2024-03-02 12:56:42.829371

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'a86473429890'
down_revision: Union[str, None] = '3604a23214eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('asa0204_01_01',
    sa.Column('psk_id', sa.Integer(), nullable=False),
    sa.Column('transaction_id', sa.Integer(), nullable=True),
    sa.Column('transaction_remarks', sa.Text(), nullable=True),
    sa.Column('api_id', sa.String(), nullable=True),
    sa.Column('app_psk_id', sa.Integer(), nullable=True),
    sa.Column('app_uid', sa.String(), nullable=True),
    sa.Column('psk_uid', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created_by', sa.String(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('cancel_by', sa.String(), nullable=True),
    sa.Column('cancel_on', sa.DateTime(), nullable=True),
    sa.Column('cancel_status', sa.String(), nullable=True),
    sa.Column('cancel_remarks', sa.String(), nullable=True),
    sa.Column('approval_level_1', sa.Integer(), nullable=True),
    sa.Column('approval_level_2', sa.Integer(), nullable=True),
    sa.Column('approval_remarks', sa.Integer(), nullable=True),
    sa.Column('workflow_id', sa.String(), nullable=True),
    sa.Column('workflow_role', sa.String(), nullable=True),
    sa.Column('row_order', sa.Integer(), nullable=True),
    sa.Column('gis_latitude', sa.Float(), nullable=True),
    sa.Column('gis_longitude', sa.Float(), nullable=True),
    sa.Column('cdn_location', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('user_type', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('reporting_to', sa.String(), nullable=True),
    sa.Column('user_groups', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('psk_id')
    )
    op.create_index(op.f('ix_asa0204_01_01_psk_id'), 'asa0204_01_01', ['psk_id'], unique=False)
    op.drop_index('ix_api_model_migrations_id', table_name='api_model_migrations')
    op.drop_table('api_model_migrations')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api_model_migrations',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('table_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('table_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('migration_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('created_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['table_id'], ['api_models.id'], name='api_model_migrations_table_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='api_model_migrations_pkey')
    )
    op.create_index('ix_api_model_migrations_id', 'api_model_migrations', ['id'], unique=False)
    op.drop_index(op.f('ix_asa0204_01_01_psk_id'), table_name='asa0204_01_01')
    op.drop_table('asa0204_01_01')
    # ### end Alembic commands ###
