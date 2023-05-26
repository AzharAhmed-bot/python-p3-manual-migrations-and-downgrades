"""Renaming students to scholars

Revision ID: 0ba6fe850944
Revises: 791279dd0760
Create Date: 2023-05-26 06:49:47.028262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ba6fe850944'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students','scholars')
    pass


def downgrade() -> None:
    op.rename_table('scholars','students')
    pass
