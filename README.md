# aind-session-json-service
REST service to connect to backend and return session json files

## Usage

### Create the server.

- The server code is developed in the aind-session-json-service-server package.
- On a push to main, a docker image will be built and published to GitHub's container registry.
- You can then run the server in a docker container or k8s pod.
- More details can be found in the [service README](aind-session-json-service-server/README.md) file

### Auto-generated client code.

- The client code is autogenerated using an openapi generator.
- On a push to main, a python library will be built and published to PyPI.
- The client can then be pip installed as `pip install aind-session-json-service-client`
- An async client can be pip installed as `pip install aind-session-json-service-async-client`
