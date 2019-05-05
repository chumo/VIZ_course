FROM continuumio/miniconda3:4.5.12

USER root

RUN apt-get update -y

RUN pip install jupyterlab matplotlib plotly cufflinks plotly_express

RUN conda install -c conda-forge nodejs

ENV NODE_OPTIONS --max-old-space-size=4096
RUN jupyter labextension install @jupyterlab/plotly-extension

ADD . /home/jovyan

VOLUME /home/jovyan/HOST
WORKDIR /home/jovyan/

EXPOSE 8888

CMD jupyter lab --ip 0.0.0.0 --allow-root --no-browser --LabApp.token=''
