# maltego-transforms
A repository containing custom maltego transforms to be used to create visual graphs.
This repository is created using the gunicorn demo from [this](https://github.com/paterva/maltego-trx) 
project.

## Description:
* custom_entities directory consists the entities created (certificate) created for the purpose of this exercise
* example graphs include the graphs created to demonstrate the custom entities and its functionalities in full 
display.
* The entities can be imported according to instructions present [here](https://docs.maltego.com/support/solutions/articles/15000010770-import-and-exporting-entities).

## Running the project:
The project is run using python-slim docker images and I've used the default docker-compose.yml to run and compose my
projects. You can this command to run build and run the project in the background:
> docker-compose up --build -d

Use this command to go to the logs:
> docker-compose logs -f

For going into the container bash use:
> docker-compose exec python bash

For production the prod.yml can be used and the compose file name need to specified in the above commands.
