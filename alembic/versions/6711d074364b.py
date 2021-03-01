"""empty message

Revision ID: 6711d074364b
Revises: 
Create Date: 2021-02-26 15:31:35.470474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6711d074364b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    
    op.drop_table('user')
    op.drop_table('menu_category')
    op.drop_table('menu_item')
    op.drop_table('inventory')
    op.drop_table('orders')
    op.drop_table('restaurant')
    op.drop_table('wishlist')
   

def downgrade():
  
    pass