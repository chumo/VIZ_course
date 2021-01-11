FROM continuumio/miniconda3:4.7.12

USER root

RUN apt-get update -y

RUN pip install notebook==6.1.6 matplotlib==3.0.3 pandas==1.2.0 plotly==4.14.2 kaleido==0.1.0

ADD . /home/jovyan

VOLUME /home/jovyan/HOST
WORKDIR /home/jovyan/

EXPOSE 8888

CMD jupyter notebook --ip 0.0.0.0 --allow-root --no-browser --NotebookApp.token=''
