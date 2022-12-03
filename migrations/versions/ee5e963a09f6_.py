"""empty message

Revision ID: ee5e963a09f6
Revises: 8f3dffe1c1a5
Create Date: 2022-12-02 22:18:10.168458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee5e963a09f6'
down_revision = '8f3dffe1c1a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('lastname',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('state',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('province',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('street',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('birthday',
               existing_type=sa.DATE(),
               nullable=True)
        batch_op.alter_column('gender',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('role',
               existing_type=sa.BOOLEAN(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('role',
               existing_type=sa.BOOLEAN(),
               nullable=False)
        batch_op.alter_column('gender',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('birthday',
               existing_type=sa.DATE(),
               nullable=False)
        batch_op.alter_column('street',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('province',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('state',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('lastname',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)

    # ### end Alembic commands ###
