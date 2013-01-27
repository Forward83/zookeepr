"""
Add block column to rego_note

Revision ID: 624cf57a935
Revises: 50062c1a43cb
Create Date: 2013-01-27 09:42:08.795162

"""

# revision identifiers, used by Alembic.
revision = '624cf57a935'
down_revision = '50062c1a43cb'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rego_note', sa.Column('block', sa.Boolean() ))
    op.execute("update rego_note set block='f'")
    op.alter_column('rego_note', 'block', nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rego_note', 'block')
    ### end Alembic commands ###
