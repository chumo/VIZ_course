FROM continuumio/anaconda3

USER root

RUN apt-get update -y

RUN pip install plotly cufflinks

RUN conda install -y -c conda-forge nodejs
RUN npm i -g npm
RUN jupyter labextension install @jupyterlab/plotly-extension
RUN jupyter labextension install jupyterlab-toc

ADD . /home/jovyan

VOLUME /home/jovyan/HOST
WORKDIR /home/jovyan/HOST

EXPOSE 8888

CMD jupyter lab --ip 0.0.0.0 --allow-root --no-browser
