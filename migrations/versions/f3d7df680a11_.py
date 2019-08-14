"""empty message

Revision ID: f3d7df680a11
Revises: 517a31284909
Create Date: 2019-08-14 00:20:32.568042

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f3d7df680a11'
down_revision = '517a31284909'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('productName', sa.String(length=45), nullable=False),
    sa.Column('productDescription', sa.String(length=255), nullable=True),
    sa.Column('productPrice', sa.String(length=45), nullable=False),
    sa.Column('productCategory', sa.String(length=45), nullable=True),
    sa.Column('productAgeRange', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('productDescription'),
    sa.UniqueConstraint('productName')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userFirstName', sa.String(length=45), nullable=False),
    sa.Column('userLastName', sa.String(length=45), nullable=False),
    sa.Column('userName', sa.String(length=45), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=45), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('userName')
    )
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userStreet', sa.String(length=45), nullable=False),
    sa.Column('userNumber', sa.String(length=45), nullable=False),
    sa.Column('userCity', sa.String(length=45), nullable=False),
    sa.Column('userState', sa.String(length=45), nullable=False),
    sa.Column('userZipCode', sa.String(length=12), nullable=False),
    sa.Column('isBillingAddress', sa.Boolean(), nullable=True),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['person_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('billing_addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('billingStreet', sa.String(length=45), nullable=True),
    sa.Column('billingNumber', sa.String(length=45), nullable=True),
    sa.Column('billingCity', sa.String(length=45), nullable=True),
    sa.Column('billingState', sa.String(length=45), nullable=True),
    sa.Column('billingZipCode', sa.String(length=12), nullable=True),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['person_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pictures',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('picture_url', sa.Text(), nullable=False),
    sa.Column('photos_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['photos_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('email', table_name='person')
    op.drop_index('username', table_name='person')
    op.drop_table('person')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('username', 'person', ['username'], unique=True)
    op.create_index('email', 'person', ['email'], unique=True)
    op.drop_table('pictures')
    op.drop_table('billing_addresses')
    op.drop_table('addresses')
    op.drop_table('users')
    op.drop_table('products')
    # ### end Alembic commands ###
