FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN apt-get update \
    && apt-get install -y --no-install-recommends jq \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*

RUN cp config.json.sample config.json

EXPOSE 4000

CMD ["./app.py"]
