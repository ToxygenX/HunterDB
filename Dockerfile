FROM python:3.9.5-buster

WORKDIR /db
RUN chmod 777 /db
RUN apt-get update -y
RUN pip3 install -U pip
COPY requirements.txt .
RUN pip3 install --no-cache-dir -U -r requirements.txt
COPY . .
CMD python3 -m db
