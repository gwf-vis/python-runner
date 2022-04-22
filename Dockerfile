FROM python:3.9-slim

RUN useradd pyrunner
USER pyrunner

WORKDIR ~/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./server.py" ]
EXPOSE 8000