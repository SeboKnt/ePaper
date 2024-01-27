FROM selenium/standalone-chrome:latest

WORKDIR /usr/src/app

USER root

RUN apt-get update && apt-get install -y \
    python3-pip \
    inetutils-ping 

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

USER seluser

CMD [ "python3", "./takeScreenshot.py" ]