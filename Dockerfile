FROM python:3.8-slim
USER root

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
ENV PORT 5050

CMD python snowplow_enrichment_api.py