FROM python:3.5.2

RUN apt-get update && \
    apt-get install -y netcat && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "dps.py"]
