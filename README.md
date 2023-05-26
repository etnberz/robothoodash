# robothoodash

A dashboard which monitors the performances of RobotHood

## Installation

To run the dashboard, you will need to set the environment variables:
ROBOTHOOD_DB_PATH: path to the robothood db.

You can install robothoodash localy by running in the robothoodash repository:

`pip install .`

## Quickstart

First build the docker image:

`docker build -t robothoodash .`

If you are in the robothoodash folder else, change . by the correct location.

To make it run:

`docker run -e ROBOTHOOD_DB_PATH=$ROBOTHOOD_DB_PATH robothoodash robothoodash/app.py


## Project status

### Current features

### Known limitations / Bugs


## Acknowledgements

### Contributors

### Miscellaneous

This project was created with the cookiecutter-python-etnberz
version [0.1.0](https://github.com/etnberz/cookie-cutter-python-etnberz/blob/v0.1.0/CHANGELOG.md).

