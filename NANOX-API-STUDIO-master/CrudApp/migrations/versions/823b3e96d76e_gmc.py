"""GMC

Revision ID: 823b3e96d76e
Revises: 
Create Date: 2023-12-15 14:53:13.463099

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '823b3e96d76e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assignmenu_roleprivilege',
    sa.Column('psk_id', sa.Integer(), nullable=False),
    sa.Column('transaction_id', sa.Integer(), nullable=True),
    sa.Column('api_id', sa.Integer(), nullable=True),
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
    sa.Column('roleid', sa.String(), nullable=True),
    sa.Column('menuid', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('psk_id')
    )
    op.create_index(op.f('ix_assignmenu_roleprivilege_psk_id'), 'assignmenu_roleprivilege', ['psk_id'], unique=False)
    op.create_table('country',
    sa.Column('psk_id', sa.Integer(), nullable=False),
    sa.Column('transaction_id', sa.Integer(), nullable=True),
    sa.Column('api_id', sa.Integer(), nullable=True),
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
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('country_code', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('psk_id')
    )
    op.create_index(op.f('ix_country_psk_id'), 'country', ['psk_id'], unique=False)
    op.create_table('gmc1201_01_01',
    sa.Column('psk_id', sa.Integer(), nullable=False),
    sa.Column('transaction_id', sa.Integer(), nullable=True),
    sa.Column('api_id', sa.Integer(), nullable=True),
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
    sa.Column('uuid', sa.String(), nullable=True),
    sa.Column('user_group_type', sa.String(), nullable=True),
    sa.Column('user_group_name', sa.String(), nullable=True),
    sa.Column('user_privilege', sa.String(), nullable=True),
    sa.Column('active', sa.String(), nullable=True),
    sa.Column('dupcheck', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('psk_id')
    )
    op.create_index(op.f('ix_gmc1201_01_01_psk_id'), 'gmc1201_01_01', ['psk_id'], unique=False)
    op.create_table('gmc1202_01_01',
    sa.Column('psk_id', sa.Integer(), nullable=False),
    sa.Column('transaction_id', sa.Integer(), nullable=True),
    sa.Column('api_id', sa.Integer(), nullable=True),
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
    sa.Column('uuid', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('user_type', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('reporting_to', sa.String(), nullable=True),
    sa.Column('user_groups', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('psk_id')
    )
    op.create_index(op.f('ix_gmc1202_01_01_psk_id'), 'gmc1202_01_01', ['psk_id'], unique=False)
    op.create_table('kommunityapi',
    sa.Column('psk_id', sa.Integer(), nullable=False),
    sa.Column('transaction_id', sa.Integer(), nullable=True),
    sa.Column('api_id', sa.Integer(), nullable=True),
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
    sa.Column('apiname', sa.String(), nullable=True),
    sa.Column('apihref', sa.String(), nullable=True),
    sa.Column('filename', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('psk_id')
    )
    op.create_index(op.f('ix_kommunityapi_psk_id'), 'kommunityapi', ['psk_id'], unique=False)
    op.create_table('menus',
    sa.Column('psk_id', sa.Integer(), nullable=False),
    sa.Column('transaction_id', sa.Integer(), nullable=True),
    sa.Column('api_id', sa.Integer(), nullable=True),
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
    sa.Column('tcode', sa.String(), nullable=True),
    sa.Column('menuname', sa.String(), nullable=True),
    sa.Column('menutype', sa.String(), nullable=True),
    sa.Column('menuhref', sa.String(), nullable=True),
    sa.Column('menuicon', sa.String(), nullable=True),
    sa.Column('parentid', sa.String(), nullable=True),
    sa.Column('menuid', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('menu_seq', sa.String(), nullable=True),
    sa.Column('menuadmin', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('psk_id')
    )
    op.create_index(op.f('ix_menus_psk_id'), 'menus', ['psk_id'], unique=False)
    op.create_table('menus_history',
    sa.Column('psk_id', sa.Integer(), nullable=False),
    sa.Column('transaction_id', sa.Integer(), nullable=True),
    sa.Column('api_id', sa.Integer(), nullable=True),
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
    sa.Column('menuname', sa.String(), nullable=True),
    sa.Column('menutype', sa.String(), nullable=True),
    sa.Column('menuhref', sa.String(), nullable=True),
    sa.Column('menuicon', sa.String(), nullable=True),
    sa.Column('parentid', sa.String(), nullable=True),
    sa.Column('menuid', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('menu_seq', sa.String(), nullable=True),
    sa.Column('menu_history_id', sa.String(), nullable=True),
    sa.Column('tcode', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('psk_id')
    )
    op.create_index(op.f('ix_menus_history_psk_id'), 'menus_history', ['psk_id'], unique=False)
    op.create_table('name',
    sa.Column('psk_id', sa.Integer(), nullable=False),
    sa.Column('transaction_id', sa.Integer(), nullable=True),
    sa.Column('api_id', sa.Integer(), nullable=True),
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
    sa.Column('docid', sa.String(), nullable=True),
    sa.Column('docdate', sa.Date(), nullable=True),
    sa.Column('secur_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('psk_id')
    )
    op.create_index(op.f('ix_name_psk_id'), 'name', ['psk_id'], unique=False)
    op.create_table('product',
    sa.Column('psk_id', sa.Integer(), nullable=False),
    sa.Column('transaction_id', sa.Integer(), nullable=True),
    sa.Column('api_id', sa.Integer(), nullable=True),
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
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('qty', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('psk_id')
    )
    op.create_index(op.f('ix_product_psk_id'), 'product', ['psk_id'], unique=False)
    op.create_table('roles',
    sa.Column('psk_id', sa.Integer(), nullable=False),
    sa.Column('transaction_id', sa.Integer(), nullable=True),
    sa.Column('api_id', sa.Integer(), nullable=True),
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
    sa.Column('rolename', sa.String(), nullable=True),
    sa.Column('roledesc', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('psk_id')
    )
    op.create_index(op.f('ix_roles_psk_id'), 'roles', ['psk_id'], unique=False)
    op.create_table('saas_application',
    sa.Column('psk_id', sa.Integer(), nullable=False),
    sa.Column('transaction_id', sa.Integer(), nullable=True),
    sa.Column('api_id', sa.Integer(), nullable=True),
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
    sa.Column('uuid', sa.String(), nullable=True),
    sa.Column('appname', sa.String(), nullable=True),
    sa.Column('appid', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('psk_id')
    )
    op.create_index(op.f('ix_saas_application_psk_id'), 'saas_application', ['psk_id'], unique=False)
    op.create_table('users',
    sa.Column('psk_id', sa.Integer(), nullable=False),
    sa.Column('transaction_id', sa.Integer(), nullable=True),
    sa.Column('api_id', sa.Integer(), nullable=True),
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
    sa.Column('firstname', sa.String(), nullable=True),
    sa.Column('lastname', sa.String(), nullable=True),
    sa.Column('mobileno', sa.String(), nullable=True),
    sa.Column('emailid', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('psk_id')
    )
    op.create_index(op.f('ix_users_psk_id'), 'users', ['psk_id'], unique=False)
    op.create_table('roleprivileges',
    sa.Column('psk_id', sa.Integer(), nullable=False),
    sa.Column('transaction_id', sa.Integer(), nullable=True),
    sa.Column('api_id', sa.Integer(), nullable=True),
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
    sa.Column('rolename', sa.String(), nullable=True),
    sa.Column('rolecode', sa.String(), nullable=True),
    sa.Column('privilege_name', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('roles_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['roles_id'], ['roles.psk_id'], ),
    sa.PrimaryKeyConstraint('psk_id')
    )
    op.create_index(op.f('ix_roleprivileges_psk_id'), 'roleprivileges', ['psk_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_roleprivileges_psk_id'), table_name='roleprivileges')
    op.drop_table('roleprivileges')
    op.drop_index(op.f('ix_users_psk_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_saas_application_psk_id'), table_name='saas_application')
    op.drop_table('saas_application')
    op.drop_index(op.f('ix_roles_psk_id'), table_name='roles')
    op.drop_table('roles')
    op.drop_index(op.f('ix_product_psk_id'), table_name='product')
    op.drop_table('product')
    op.drop_index(op.f('ix_name_psk_id'), table_name='name')
    op.drop_table('name')
    op.drop_index(op.f('ix_menus_history_psk_id'), table_name='menus_history')
    op.drop_table('menus_history')
    op.drop_index(op.f('ix_menus_psk_id'), table_name='menus')
    op.drop_table('menus')
    op.drop_index(op.f('ix_kommunityapi_psk_id'), table_name='kommunityapi')
    op.drop_table('kommunityapi')
    op.drop_index(op.f('ix_gmc1202_01_01_psk_id'), table_name='gmc1202_01_01')
    op.drop_table('gmc1202_01_01')
    op.drop_index(op.f('ix_gmc1201_01_01_psk_id'), table_name='gmc1201_01_01')
    op.drop_table('gmc1201_01_01')
    op.drop_index(op.f('ix_country_psk_id'), table_name='country')
    op.drop_table('country')
    op.drop_index(op.f('ix_assignmenu_roleprivilege_psk_id'), table_name='assignmenu_roleprivilege')
    op.drop_table('assignmenu_roleprivilege')
    # ### end Alembic commands ###
