FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ENV PYTHONUNBUFFERED=1

# 1. Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

# 2. Set the entrypoint for the container
ENTRYPOINT ["/app/entrypoint.sh"]

# 3. The CMD is now passed as arguments to the ENTRYPOINT
CMD ["gunicorn","-k", "uvicorn.workers.UvicornWorker", "--workers", "2", "--worker-tmp-dir", "/dev/shm", "--threads", "1", "--timeout", "60", "--keep-alive", "75", "main:app", "-b", "0.0.0.0:8000"]