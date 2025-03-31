# Docker-FastAPI

This project is a FastAPI application running inside a Docker container. The application primarily uses FastAPI to connect to a MongoDB database via `pymongo.MongoClient`, allowing data retrieval and insertion into the database.

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
    DB_USERNAME=YOUR_USERNAME
    DB_ PASSWORD=YOUR_PASSWORD

    DB_ADDRESS = mongodb://YOUR_USERNAME:YOUR_PASSWORD@mongo:27017/
    DB_NAME = YOUR_DATABASE_NAME
    DB_USER_COLLECTION = YOUR_USER_COLLECTION
    DB_DATA_COLLECTION = YOUR_DATA_COLLECTION
    ```

## Running the Application

To run the FastAPI app with Docker, use the following command:

```bash
docker compose up
```

## API Request Templates

A Jupyter Notebook (`fast_api.ipynb`) containing example GET and POST request templates is available in the main directory. You can use it to test API endpoints easily.

For detailed API usage, refer to the notebook for step-by-step request examples.

