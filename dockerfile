# Use official Python image (lightweight)
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first (for better caching)
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN pip install --no-cache-dir \
    pydantic[email] \
    python-jose[cryptography] \
    uvicorn fastapi sqlalchemy pydantic passlib jose[cryptography] \
    python-multipart  # Ensure python-multipart is installed

# Copy the entire project code
COPY . .

# Expose FastAPI default port
EXPOSE 8000

# Run the application using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
