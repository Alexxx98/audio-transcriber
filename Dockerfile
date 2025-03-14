FROM python:3.13.2-alpine

WORKDIR /transcriber

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:5001", "app:app"]
