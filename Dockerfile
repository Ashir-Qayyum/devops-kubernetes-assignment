FROM python:3.9

WORKDIR /app

COPY python-basic-app.py requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python3", "python-basic-app.py"]

