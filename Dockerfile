FROM python:3.7
RUN mkdir /home/etl
COPY . /home/etl
RUN wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public | apt-key add - && \
    apt update && \
    apt -y install software-properties-common && \
    add-apt-repository --yes https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/ && \
    apt update && \
    apt -y upgrade && \
    apt -y install pipenv adoptopenjdk-8-hotspot && \
    export JAVA_HOME=/usr/lib/jvm/adoptopenjdk-8-hotspot-amd64/ && \
    cd /home/etl && \
    pipenv install --dev