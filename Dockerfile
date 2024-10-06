FROM python:3.9-alpine

WORKDIR /iap1-tema

EXPOSE 5000

COPY ./requirements.txt requirements.txt

RUN  pip install -r requirements.txt

COPY ./main.py main.py

COPY ./website/ website/

CMD ["python3", "main.py"]
