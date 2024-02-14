FROM centos:7
LABEL MAINTAINER="hwakabh"

WORKDIR /tmp

RUN set -x && \
    yum -y install wget && \
    yum -y install git && \
    yum -y install https://centos7.iuscommunity.org/ius-release.rpm && \
    yum -y install python34u python34u-libs python34u-devel python34-pip && \
    wget https://rpm.nodesource.com/setup_13.x && \
    chmod 744 ./setup_13.x && \
    /bin/bash ./setup_13.x && \
    yum -y install gcc-c++ make nodejs
