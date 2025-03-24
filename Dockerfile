FROM python:3.12-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip

CMD ["python", "MediaAluno.py"]
