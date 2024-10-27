FROM python:3.13-bookworm

ENV PYTHONUNBEFFERED=1

ARG UID
ARG GID

RUN groupadd --gid $GID app
RUN useradd --uid $UID --gid app --shell /bin/bash -d /app app

RUN  pip install --no-cache-dir poetry=='1.8.4'

COPY backend/pyproject.toml backend/poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install

WORKDIR /app
USER app
