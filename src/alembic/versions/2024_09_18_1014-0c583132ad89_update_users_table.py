"""update users table

Revision ID: 0c583132ad89
Revises: f213a7be30fa
Create Date: 2024-09-18 10:14:17.676173

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "0c583132ad89"
down_revision: Union[str, None] = "f213a7be30fa"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("foo", sa.Integer(), nullable=False))
    op.add_column("users", sa.Column("bar", sa.Integer(), nullable=False))
    op.create_unique_constraint(
        op.f("uq_users_foo_bar"), "users", ["foo", "bar"]
    )


def downgrade() -> None:
    op.drop_constraint(op.f("uq_users_foo_bar"), "users", type_="unique")
    op.drop_column("users", "bar")
    op.drop_column("users", "foo")
