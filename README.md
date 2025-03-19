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

2. Create a `.env` file in the project root directory with the following content:
    ```dotenv
    DB_NAME=your_database_name
    DB_COLLECTION=your_collection_name
    ```

## Running the Application

To run the FastAPI app with Docker, use the following command:

```bash
docker compose up
