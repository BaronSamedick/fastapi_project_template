"""update users table

Revision ID: 477320b44ab7
Revises: f213a7be30fa
Create Date: 2024-09-17 17:54:29.460096

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "477320b44ab7"
down_revision: Union[str, None] = "f213a7be30fa"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("foo", sa.Integer(), nullable=False))
    op.add_column("users", sa.Column("bar", sa.Integer(), nullable=False))
    op.create_unique_constraint(op.f("uq_users_foo"), "users", ["foo", "bar"])


def downgrade() -> None:
    op.drop_constraint(op.f("uq_users_foo"), "users", type_="unique")
    op.drop_column("users", "bar")
    op.drop_column("users", "foo")
