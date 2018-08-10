## Build:

docker build -t plotlydev .

Use --no-cache if you want to build from scratch.

## Run:
cd # if you want to serve from the HOME directory
docker run --rm -p 6868:8888 -it -v $PWD:/home/jovyan/HOST plotlydev bash

and inside the Docker image, execute:

sh run-lab.sh
