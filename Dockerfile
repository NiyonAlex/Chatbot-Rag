FROM python:3.11.3

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

RUN python -m spacy download en_core_web_sm

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]