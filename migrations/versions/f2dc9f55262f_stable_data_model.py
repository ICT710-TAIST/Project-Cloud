"""stable data model

Revision ID: f2dc9f55262f
Revises: 0d9279a13b2a
Create Date: 2020-03-31 17:06:34.381140

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f2dc9f55262f'
down_revision = '0d9279a13b2a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sensor_data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sensor_data',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('device_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('roll', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pitch', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('yaw', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('acc_x', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('acc_y', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('acc_z', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('label', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='sensor_data_pkey')
    )
    # ### end Alembic commands ###