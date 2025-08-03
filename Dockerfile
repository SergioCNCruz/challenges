FROM python:3.9-slim

WORKDIR /app

ENV POETRY_VERSION=2.1.3 \
    PYTHONPATH=/app/src

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-root || true

COPY . /app

CMD ["uvicorn", "scraper_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
