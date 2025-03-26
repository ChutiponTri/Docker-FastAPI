# Docker-FastAPI

This project is a FastAPI application running inside a Docker container.

## Prerequisites

Ensure you have the following installed on your machine:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/docker-fastapi.git
    cd docker-fastapi
    ```

2. Copy the `env.template.txt` file to a new file named `.env` in the project root directory:
    ```bash
    cp env.template.txt .env
    ```

3. Edit the `.env` file to configure your MongoDB settings:
    ```dotenv
    USERNAME=root
    PASSWORD=example

    DB_ADDRESS = mongodb://root:example@mongo:27017/
    DB_NAME = preme
    DB_USER_COLLECTION = user
    DB_DATA_COLLECTION = data

    MONGO_INITDB_ROOT_USERNAME = root
    MONGO_INITDB_ROOT_PASSWORD = example

    ME_CONFIG_MONGODB_ADMINUSERNAME = root
    ME_CONFIG_MONGODB_ADMINPASSWORD = example
    ME_CONFIG_MONGODB_URL = mongodb://root:example@mongo:27017/
    ME_CONFIG_BASICAUTH = false
    ```

## Running the Application

To run the FastAPI app with Docker, use the following command:

```bash
docker compose up
```

## API Request Templates

A Jupyter Notebook (`fast_api.ipynb`) containing example GET and POST request templates is available in the main directory. You can use it to test API endpoints easily.

For detailed API usage, refer to the notebook for step-by-step request examples.

