"""create user table

Revision ID: 3759194b9adf
Revises: 
Create Date: 2024-06-28 17:00:38.258039

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "3759194b9adf"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("username"),
    )


def downgrade() -> None:
    op.drop_table("users")
