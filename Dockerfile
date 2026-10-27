FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install only the server dependencies (the `agent` group is not needed here).
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-default-groups --no-install-project

COPY servers ./servers

EXPOSE 8000
CMD ["uv", "run", "--no-sync", "python", "servers/demo/server.py"]
