from enum import StrEnum

from pydantic import BaseModel


class RequestModel(BaseModel):
    model: str
    prompt: str


class AvailableModels(StrEnum):
    model_1 = "gpt-3.5-turbo"
    model_2 = "gpt-4-1106-preview"
    model_3 = "gpt-4o"
    model_4 = "Llama-2-70B-Chat"
    model_5 = "Meta-Llama-3-70b-Instruct"
    model_6 = "Mixtral-8x7B-Instruct"
    model_7 = "MPT-7B-Instruct"
    model_8 = "MPT-30B-Instruct"
    model_9 = "DBRX-Instruct"
    model_10 = "Owl_WGU_Program_Advisor_BA"
    model_11 = "Owl_MTC_Enrollment_Counselor"
    model_12 = "Owl_WGU_Smart_Statistics_TA"
    model_13 = "Owl_WGU_Smart_History_TA"
    model_14 = "Owl_WGU_Smart_English_TA"
    model_15 = "Owl_ChatLR"
