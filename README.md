# `langchain-test-project-abcde`

<!--- This is a LangChain project bootstrapped by [LangChain CLI](https://github.com/langchain-ai/langchain). --->

## Customise

To customise this project, edit the following files:

- `langchain_test_project_abcde/chain.py` contains an example chain, which you can edit to suit your needs.
- `langchain_test_project_abcde/server.py` contains a FastAPI app that serves that chain using `langserve`. You can edit this to add more endpoints or customise your server.
- `tests/test_chain.py` contains tests for the chain. You can edit this to add more tests.
- `pyproject.toml` contains the project metadata, including the project name, version, and dependencies. You can edit this to add more dependencies or customise your project metadata.

## Install dependencies

```bash
poetry install
```

## Usage

To run the project locally, run

```
make start
```

This will launch a webserver on port 8000.

## Deploy

To deploy the project, first build the docker image:

```
docker build . -t langchain_test_project_abcde:latest
```

Then run the image:

```
docker run -p 8000:8000 langchain_test_project_abcde:latest
```

## Contributing

For information on how to set up your dev environment and contribute, see [here](.github/CONTRIBUTING.md).
