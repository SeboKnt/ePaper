FROM seleniarm/standalone-firefox:latest

WORKDIR /usr/src/app

USER root

ENV DEBIAN_FRONTEND=noninteractive
RUN echo 'libc6 hold' | dpkg --set-selections

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    inetutils-ping 

COPY requirements.txt ./

RUN python3 -m venv venv
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

COPY . .

USER seluser

CMD [ "venv/bin/python3", "./takeScreenshot.py" ]