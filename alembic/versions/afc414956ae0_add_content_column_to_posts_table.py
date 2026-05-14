"""add content column to posts table

Revision ID: afc414956ae0
Revises: 7bb7f0c534d4
Create Date: 2026-05-14 17:05:01.308934

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'afc414956ae0'
down_revision: Union[str, Sequence[str], None] = '7bb7f0c534d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
