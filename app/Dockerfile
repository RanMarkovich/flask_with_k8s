FROM python:3.10-slim
COPY . .
RUN pip install --upgrade pip && pip install flask
EXPOSE 5000
CMD python app/app.py
