"""add foreign key to posts table

Revision ID: 05fba66ca053
Revises: 8883a1bffc01
Create Date: 2026-05-14 18:23:52.489404

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '05fba66ca053'
down_revision: Union[str, Sequence[str], None] = '8883a1bffc01'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_user_fk', source_table="posts", referent_table="users", local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk',table_name="posts")
    op.drop_column('posts','owner_id')
    pass
