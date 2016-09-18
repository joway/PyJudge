FROM ubuntu:14.04

ENV IMAGE_NAME "UBUNTU-BASE"
ENV VERSION 0.0.1

RUN apt-get -qq update

RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python3-software-properties software-properties-common

# tools
RUN apt-get -y install \
    build-essential \
    byobu curl git htop man unzip vim wget

# language support
RUN apt-get -y install \
#   python
    python-setuptools \
    python-dev \
    python-pip \
#   c && cpp
    gcc \
    g++ \
#   java
    openjdk-7-jdk

#   clean
RUN rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64

RUN mkdir /output \
 && mkdir /input \
 && mkdir /scripts

ADD ./scripts/*.* /scripts/
RUN chmod +x /scripts/*.sh

WORKDIR /scripts

VOLUME /input /output
