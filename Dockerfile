# Use the official Python image from the Docker Hub
FROM python:3.10.12

# Set the working directory in the container
WORKDIR /app

# Install dependencies for Poetry
RUN apt-get update && apt-get install -y curl

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:${PATH}"

# Copy the pyproject.toml and poetry.lock files to the container
COPY pyproject.toml ./
# COPY poetry.lock ./  # Uncomment this line if you have a poetry.lock file

# Install the project dependencies
RUN poetry install --no-root

# Copy the rest of the application code to the container
COPY . .
# Command to run the application
CMD ["poetry", "run", "python", "ingestion.py"]
