FROM nvidia/cuda:12.3.2-devel-ubuntu22.04

RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv \
    git curl build-essential libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

ENV POETRY_VERSION=1.8.2
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /workspaces/code

COPY pyproject.toml ./
RUN poetry config virtualenvs.create false \
 && poetry install --no-root

COPY . .

ENV PYTHONUNBUFFERED=1
