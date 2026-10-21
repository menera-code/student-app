FROM python:3-alpine
WORKDIR /app
COPY app.py .
CMD ["python", "-u", "app.py"]
