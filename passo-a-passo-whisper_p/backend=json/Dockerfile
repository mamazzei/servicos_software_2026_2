from python:3.11-slim

WORKDIR /code

RUN apt-get update \
    && apt-get install =y --no-install-recommends \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# 1º as dependências - camada estável
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r \
    /code/requirements.txt

# 2º o código = camada volátil

COPY ./app /code/app
EXPOSE 8080

CMD ["uvicorn", "app.main:app", \
    "--host", "0.0.0.0", "--port", "8080"]

    
