FROM python:3.11-slim
WORKDIR /code
RUN pip install --no-cache-dir fastapi uvicorn psycopg2-binary pydantic
COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]