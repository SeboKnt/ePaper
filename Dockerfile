FROM python:3.9

WORKDIR /app

RUN apt update && apt upgrade -y
RUN apt-get install libopenjp2-7 automake iputils-ping -y
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

COPY chromedriver /app/chromedriver
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

COPY takeScreenshot.py /app/takeScreenshot.py

CMD ["python3", "/app/takeScreenshot.py"]