"""Renaming students to Scholars

Revision ID: 50fe9f1098ff
Revises: 15c88a86cf95
Create Date: 2023-05-26 06:58:58.726371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50fe9f1098ff'
down_revision = '15c88a86cf95'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_table('scholars')
    pass


def downgrade() -> None:
    op.create_table('scholars')
    pass
