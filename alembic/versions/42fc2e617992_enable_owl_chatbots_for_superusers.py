"""Enable Owl chatbots for superusers.

Revision ID: 42fc2e617992
Revises: 8f344217cd59
Create Date: 2024-05-18 13:38:30.977226

"""

from alembic import op
import sqlalchemy as sa

available_models = [
    "gpt-3.5-turbo",
    "gpt-4-1106-preview",
    "Llama2-70B",
    "Mixtral-8x7B",
    "MPT-7B-Instruct",
    "MPT-30B-Instruct",
    "Owl_WGU_Program_Advisor_BA",
    "Owl_MTC_Enrollment_Counselor",
    "Owl_WGU_Smart_Statistics_TA",
    "Owl_WGU_Smart_History_TA",
]
available_models_for_not_superusers = [
    "gpt-3.5-turbo",
    "gpt-4-1106-preview",
    "Llama2-70B",
    "Mixtral-8x7B",
    "MPT-7B-Instruct",
    "MPT-30B-Instruct",
]
available_models_str = ", ".join([f"'{model}'" for model in available_models])
available_models_for_not_superusers_str = ", ".join(
    [f"'{model}'" for model in available_models_for_not_superusers]
)

# revision identifiers, used by Alembic.
revision = "42fc2e617992"
down_revision = "8f344217cd59"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        f"""
                UPDATE "user"
                SET available_models = CASE 
                	WHEN is_admin = false THEN ARRAY[{available_models_for_not_superusers_str}]
                	ELSE ARRAY[{available_models_str}]
                END;
               """
    )


def downgrade() -> None:
    op.execute(
        f"""
               UPDATE "user"
               SET available_models = ARRAY[{available_models_str}]
               """
    )
