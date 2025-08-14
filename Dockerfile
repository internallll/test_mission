FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq-dev \
    gcc \
    python3-dev \
    postgresql-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/
WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD ./ /app/
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
