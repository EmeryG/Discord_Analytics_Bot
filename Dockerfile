FROM python:3.9-slim
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
COPY /src /src
COPY /src/db /src/db


CMD [ "python3" , "/src/app.py" ]