FROM python:3.8-buster

# working directory
WORKDIR /usr/src/app

RUN pip install pytest

COPY . .

RUN python -m pytest

ENTRYPOINT ["python", "./wordle_assist.py"]