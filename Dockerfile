FROM python:3.9

WORKDIR /usr/src/app

COPY . ./

RUN pip install poetry
RUN pip install datasets
RUN poetry install

CMD ["python", "./llm_code_generation_main.py"]
