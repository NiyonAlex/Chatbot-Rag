from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/ui/templates")

public_models = [
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
