FROM continuumio/miniconda3:4.10.3

USER root

RUN apt-get update -y

RUN pip install notebook==6.4.5 matplotlib==3.4.3 pandas==1.3.4 plotly==5.3.1 kaleido==0.2.1

ADD . /home/jovyan

VOLUME /home/jovyan/HOST
WORKDIR /home/jovyan/

EXPOSE 8888

CMD jupyter notebook --ip 0.0.0.0 --allow-root --no-browser --NotebookApp.token=''
