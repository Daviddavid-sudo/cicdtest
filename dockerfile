FROM python:3.12-slim
WORKDIR /app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY src/ ./src
COPY tests/ ./tests/
COPY data/ ./data/

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD ["pytest"]
