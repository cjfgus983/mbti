"""empty message

Revision ID: f9df811e0235
Revises: cff85af477c5
Create Date: 2022-05-23 19:09:09.973937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9df811e0235'
down_revision = 'cff85af477c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.drop_constraint('fk_comment_gomin_id_gomin', type_='foreignkey')
        batch_op.drop_column('gomin_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('gomin_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_comment_gomin_id_gomin', 'gomin', ['gomin_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###
