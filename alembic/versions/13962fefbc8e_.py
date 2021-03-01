"""empty message

Revision ID: 13962fefbc8e
Revises: 6711d074364b
Create Date: 2021-02-26 22:45:47.225963

"""
from enum import unique
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13962fefbc8e'
down_revision = '6711d074364b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('wishlist',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('name', sa.VARCHAR(), nullable=False),
                    sa.Column('description', sa.VARCHAR(), nullable=True),
                    sa.Column('no_of_votes', sa.INTEGER(), nullable=True),
                    sa.Column('categoryid', sa.INTEGER(), nullable=False),
                    sa.ForeignKeyConstraint(['categoryid'], ['menu_category.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('restaurant',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('name', sa.VARCHAR(), nullable=False),
                    sa.Column('address', sa.VARCHAR(), nullable=True),
                    sa.Column('open_time', sa.DATETIME(), nullable=True),
                    sa.Column('close_time', sa.DATETIME(), nullable=True),
                    sa.Column('rating', sa.INTEGER(), nullable=True),
                    sa.Column('average_cost', sa.INTEGER(), nullable=False),
                    sa.Column('userid', sa.INTEGER(), nullable=False),
                    sa.ForeignKeyConstraint(['userid'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('address')
                    )
    op.create_table('orders',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('userid', sa.INTEGER(), nullable=False),
                    sa.Column('restid', sa.INTEGER(), nullable=False),
                    sa.Column('description', sa.VARCHAR(), nullable=True),
                    sa.Column('date', sa.DATETIME(), nullable=False),
                    sa.Column('itemid', sa.INTEGER(), nullable=False),
                    sa.Column('quantity', sa.INTEGER(), nullable=False),
                    sa.ForeignKeyConstraint(['itemid'], ['menu_item.id'], ),
                    sa.ForeignKeyConstraint(['restid'], ['restaurant.id'], ),
                    sa.ForeignKeyConstraint(['userid'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('inventory',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    # sa.Column('name', sa.VARCHAR(), nullable=False),
                    sa.Column('quantity', sa.INTEGER(), nullable=False),
                    sa.Column('itemid', sa.VARCHAR(), nullable=False),
                    sa.Column('restaurantid', sa.INTEGER(), nullable=False),
                    sa.ForeignKeyConstraint(['itemid'], ['menu_item.id'], ),
                    sa.ForeignKeyConstraint(['restaurantid'], ['restaurant.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('menu_item',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('categid', sa.INTEGER(), nullable=False),
                    sa.Column('name', sa.VARCHAR(), nullable=False),
                    sa.Column('description', sa.VARCHAR(), nullable=True),
                    sa.Column('cost', sa.INTEGER(), nullable=False),
                    sa.Column('gluten_free', sa.VARCHAR(), nullable=True),
                    sa.Column('vegetarian', sa.VARCHAR(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['categid'], ['menu_category.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    op.create_table('menu_category',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('name', sa.VARCHAR(), nullable=False),
                    sa.Column('description', sa.VARCHAR(), nullable=True),
                    sa.Column('restid', sa.INTEGER(), nullable=False),
                    sa.ForeignKeyConstraint(['restid'], ['restaurant.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('user',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('name', sa.VARCHAR(), nullable=False),
                    sa.Column('email', sa.VARCHAR(), nullable=False,unique=True),
                    sa.Column('password', sa.VARCHAR(), nullable=False),
                    sa.Column('age', sa.INTEGER(), nullable=True),
                    sa.Column('mobile', sa.INTEGER(), nullable=True,unique=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('mobile')
                    )


def downgrade():
    pass
