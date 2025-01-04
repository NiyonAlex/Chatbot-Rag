"""Create available_model for User column.

Revision ID: 8f344217cd59
Revises: 
Create Date: 2024-04-20 14:15:02.458544

"""
from alembic import op
import sqlalchemy as sa

from app.apis.models.request_model import AvailableModels
available_models_str = ", ".join([f"'{model.value}'" for model in AvailableModels])

# revision identifiers, used by Alembic.
revision = '8f344217cd59'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("user", sa.Column("available_models", sa.ARRAY(sa.Text()), nullable=True))
    op.execute(f"""
               UPDATE "user"
               SET available_models = ARRAY[{available_models_str}]
               """)
    # we want nullable=False for models
    op.alter_column("user","available_models",nullable=False)

def downgrade() -> None:
    op.drop_column("user", "available_models")
