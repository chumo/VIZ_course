FROM continuumio/miniconda3:4.7.10

USER root

RUN apt-get update -y
RUN apt-get install -y xvfb libgtk2.0-0 libgconf-2-4 gnupg2

RUN pip install jupyterlab matplotlib==3.0.3 pandas==0.25.1 plotly==4.1.1

# Needed to export to static images
#RUN conda install -c plotly plotly-orca
RUN conda install -y psutil==5.6.3

# Needed to run Plotly in JupyterLab
RUN conda install -c conda-forge nodejs
ENV NODE_OPTIONS --max-old-space-size=4096
RUN jupyter labextension install @jupyterlab/plotly-extension

# google chrome (needed for orca)
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update -y && \
    apt-get install -y google-chrome-stable

#https://stackoverflow.com/questions/54112336/docker-and-plotly
# Download orca AppImage, extract it, and make it executable under xvfb
RUN wget -P /home https://github.com/plotly/orca/releases/download/v1.2.1/orca-1.2.1-x86_64.AppImage
RUN chmod 777 /home/orca-1.2.1-x86_64.AppImage
# To avoid the need for FUSE, extract the AppImage into a directory (name squashfs-root by default)
RUN cd /home && /home/orca-1.2.1-x86_64.AppImage --appimage-extract
RUN printf '#!/bin/bash \nxvfb-run --auto-servernum --server-args "-screen 0 640x480x24" /home/squashfs-root/app/orca "$@"' > /usr/bin/orca
RUN chmod 777 /usr/bin/orca
RUN chmod -R 777 /home/squashfs-root/


ADD . /home/jovyan

VOLUME /home/jovyan/HOST
WORKDIR /home/jovyan/

EXPOSE 8888

CMD jupyter lab --ip 0.0.0.0 --allow-root --no-browser --LabApp.token=''
