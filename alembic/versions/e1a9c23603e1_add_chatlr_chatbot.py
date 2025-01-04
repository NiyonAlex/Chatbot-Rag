"""Add ChatLR chatbot.

Revision ID: e1a9c23603e1
Revises: 2f113b03cd38
Create Date: 2024-05-29 14:59:40.642514

"""

from alembic import op
import sqlalchemy as sa

new_model = "Owl_ChatLR"
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
    "Owl_WGU_Smart_English_TA",
] + [new_model]
available_models_str = ", ".join([f"'{model}'" for model in available_models])
available_models.remove(new_model)
init_available_models_str = ", ".join([f"'{model}'" for model in available_models])

# revision identifiers, used by Alembic.
revision = "e1a9c23603e1"
down_revision = "2f113b03cd38"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        f"""
                UPDATE "user"
                SET available_models = CASE 
                	WHEN is_admin = true THEN ARRAY[{available_models_str}]
                	ELSE available_models
                END;
               """
    )


def downgrade() -> None:
    op.execute(
        f"""
                UPDATE "user"
                SET available_models = CASE 
                	WHEN is_admin = true THEN ARRAY[{init_available_models_str}]
                	ELSE available_models
                END;
               """
    )
