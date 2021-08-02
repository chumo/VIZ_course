FROM continuumio/miniconda3:4.9.2

USER root

RUN apt-get update -y

RUN pip install notebook==6.3.0 matplotlib==3.4.2 pandas==1.2.4 plotly==4.14.3 kaleido==0.2.1

ADD . /home/jovyan

VOLUME /home/jovyan/HOST
WORKDIR /home/jovyan/

EXPOSE 8888

CMD jupyter notebook --ip 0.0.0.0 --allow-root --no-browser --NotebookApp.token=''
