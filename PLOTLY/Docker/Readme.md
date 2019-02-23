# plotly_course

This Docker image starts a JupyterLab server and contains the plotly and cufflinks libraries,
as weel as the python libraries in miniconda distribution (numpy, pandas, etc). The plotly extension
is also installed so that plotly plots can show up inline in the JupyterLab.

## Build:

An image already built exists in Docker Hub, so there is no need to build the image.
Still you can build it locally using:

`docker build -t plotly_course .`

Use `--no-cache` if you want to build from scratch.

## Run:

```
cd # if you want to serve from the HOME directory
docker run --rm -it -p 1789:8888 -v $PWD:/home/jovyan/HOST chumo/plotly_course
```

```
modifiers explained:

--rm : to remove the Docker container after finishing the JupyterLab server with CTRL+c.
 -it : to be able to stop the JupyterLab server running on the container.
 -p  : to map the port 8888 internal to the running container (where JypyterLab is running) to the port 1789 outside the container.
 -v  : to mount a local directory into the directory /home/jovyan/HOST inside the container.

```

## Access the Jupyter Lab at:

http://localhost:1789

