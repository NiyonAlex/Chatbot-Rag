"""Add Llama3, DBRX, and GPT-4o

Revision ID: ed79ba65f846
Revises: e1a9c23603e1
Create Date: 2024-07-03 14:33:30.341765

"""

from alembic import op
import sqlalchemy as sa


available_models = [
    "gpt-3.5-turbo",
    "gpt-4-1106-preview",
    "gpt-4o",
    "Llama-2-70B-Chat",
    "Meta-Llama-3-70b-Instruct",
    "Mixtral-8x7B-Instruct",
    "MPT-7B-Instruct",
    "MPT-30B-Instruct",
    "DBRX-Instruct",
    "Owl_WGU_Program_Advisor_BA",
    "Owl_MTC_Enrollment_Counselor",
    "Owl_WGU_Smart_Statistics_TA",
    "Owl_WGU_Smart_History_TA",
    "Owl_WGU_Smart_English_TA",
    "Owl_ChatLR",
]
available_models_for_not_superusers = [
    "gpt-3.5-turbo",
    "gpt-4-1106-preview",
    "gpt-4o",
    "Llama-2-70B-Chat",
    "Meta-Llama-3-70b-Instruct",
    "Mixtral-8x7B-Instruct",
    "MPT-7B-Instruct",
    "MPT-30B-Instruct",
    "DBRX-Instruct",
]
available_models_str = ", ".join([f"'{model}'" for model in available_models])
available_models_for_not_superusers_str = ", ".join(
    [f"'{model}'" for model in available_models_for_not_superusers]
)

# revision identifiers, used by Alembic.
revision = "ed79ba65f846"
down_revision = "e1a9c23603e1"
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
