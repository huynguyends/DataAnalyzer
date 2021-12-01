FROM python:3.9.7
EXPOSE 8501

COPY requirements.txt ./
COPY /app ./app
COPY /src ./src


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD []
