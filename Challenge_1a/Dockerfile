FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

COPY process_pdfs.py /app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# Do NOT copy PDFs or outputs during build
# These are mounted at runtime via `docker run`

ENTRYPOINT ["python", "process_pdfs.py"]
