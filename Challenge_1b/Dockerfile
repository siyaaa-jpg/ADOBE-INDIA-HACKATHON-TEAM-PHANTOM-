FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY process_documents.py /app/
COPY Collection1 /app/Collection1
COPY Collection2 /app/Collection2
COPY Collection3 /app/Collection3


ENTRYPOINT ["python", "process_documents.py"]
