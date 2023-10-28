"""empty message

Revision ID: 4c7ab9dd7812
Revises: 0ce3b0807cea
Create Date: 2023-10-28 23:02:39.445550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c7ab9dd7812'
down_revision = '0ce3b0807cea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pos__mod', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'categ', ['category'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pos__mod', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('category')

    # ### end Alembic commands ###