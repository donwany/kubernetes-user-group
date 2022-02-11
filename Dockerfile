FROM python:3-alpine
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 23321
CMD ["python", "app.py"]
