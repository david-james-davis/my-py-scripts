# Use the Wolfi base image
FROM cgr.dev/chainguard/wolfi-base

# Set the desired Python version
ARG PYTHON_VERSION=3.13

# Install Python and pip
RUN apk add --no-cache python-${PYTHON_VERSION} py${PYTHON_VERSION}-pip

# Install Poetry using pip
RUN pip install poetry

# Set up a working directory
WORKDIR /app

# Copy the entire project first
COPY . .

# Make scripts executable
RUN chmod +x scripts/*.py

# Install dependencies (without virtual environments)
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root

# Default command, which can be overridden at runtime
CMD ["poetry", "run", "python"]