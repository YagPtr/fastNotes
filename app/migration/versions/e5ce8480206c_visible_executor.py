"""+visible+executor

Revision ID: e5ce8480206c
Revises: 53dd9fe8f992
Create Date: 2025-02-07 09:34:08.702305

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e5ce8480206c"
down_revision: Union[str, None] = "53dd9fe8f992"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "note_database", sa.Column("visible", sa.Boolean(True), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("note_database", "visible")
    # ### end Alembic commands ###
