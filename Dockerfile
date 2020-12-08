FROM  python:3.8

WORKDIR /django

COPY requirements.txt ./

RUN python -m pip install -U pip && pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]