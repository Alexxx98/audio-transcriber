FROM python:3.13.2-alpine

WORKDIR /transcriber

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:5001", "--timeout", "3600", "app:app"]
