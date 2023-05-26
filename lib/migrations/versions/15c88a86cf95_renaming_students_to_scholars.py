"""Renaming students to Scholars

Revision ID: 15c88a86cf95
Revises: 0ba6fe850944
Create Date: 2023-05-26 06:55:32.435853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15c88a86cf95'
down_revision = '0ba6fe850944'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students','Scholars')
    pass


def downgrade() -> None:
    op.rename_table('Scholars','students')
    pass
