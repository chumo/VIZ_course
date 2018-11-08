FROM continuumio/anaconda3:5.3.0

USER root

RUN apt-get update -y

RUN pip install plotly cufflinks

# Use node 8 as the lastest node brings problem to install jupyter labextensions
RUN apt-get install -y sudo gnupg2
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
RUN apt-get install -y nodejs yarn

ENV NODE_OPTIONS --max-old-space-size=4096
RUN jupyter labextension install @jupyterlab/plotly-extension

ADD . /home/jovyan

VOLUME /home/jovyan/HOST
WORKDIR /home/jovyan/

EXPOSE 8888

CMD jupyter lab --ip 0.0.0.0 --allow-root --no-browser
