# Smart-Owl for local development guide

## Prerequisites

Before you begin, ensure you have installed:

- Docker
- Docker Compose
- AWS CLI
- Python 3.11.3 (or the Python version referenced in the `Dockerfile`)
- DBeaver or another database GUI tool for PostgresQL

## Getting Started

### 0. Python environment setup

- (optional) `pyenv local 3.11.3` This command set python version 3.11.3 only for the project
- (optional) `python --version` Check if `python 3.11.3` is set for the project
- (optional) `python -m venv venv` Will creat venv environment
- (optional) `source venv/Scripts/activate` Will activate venv environment (need to check path)

### 1. Clone the repository and install python libraries

- `git clone https://github.com/WGU-edu/smart-owl`
- `cd smart-owl`
- `pip install --no-cache-dir --upgrade -r requirements.txt`

### 2. Create an environment file for the project

- Create a file named `.env` inside the project root directory and add the following content

  ```
  # AWS
  AWS_REGION=us-west-2

  # DynamoDB
  DYNAMO_DB_TABLE=openai-call-log
  DYNAMO_DB_ENDPOINT=http://localhost:8000

  # OpenAI
  OPEN_AI_KEY=[[OPENAI KEY HERE]]

  # PostgreSQL
  POSTGRES_USER=user
  POSTGRES_PASSWORD=password
  POSTGRES_SERVER=localhost
  POSTGRES_PORT=5432
  POSTGRES_DB=chatbot-rag

  # Redis
  REDIS_HOST=localhost
  REDIS_PORT=6379

  ##### DATABRICKS #####

  DATABRICKS_HOST=https://wgu-prod.cloud.databricks.com
  ENVIRONMENT=dev

  # Service principal: "dev"
  DATABRICKS_SP_CLIENT_ID=[[SP CLIENT ID HERE]]
  DATABRICKS_SP_SECRET=[[SP SECRET HERE]]
  ```

### 3. AWS profile configuration

- Add the following profile to the file `~/.aws/config`

  ```
  [profile local]
  region = us-west-2
  output = json
  ```

- Add the following credentials for the `local` profile to `~/.aws/credentials`
  ```
  [local]
  aws_access_key_id = accesskeyid
  aws_secret_access_key = secretaccesskey
  ```

### 4. Add a superuser to `user` table

- Comment some parts in source code in order to manually add a superuser via Swagger UI (this part should be reverted after adding a superuser)

  - `app/db/models/user.py` -> comment for `available_models`
  - `app/apis/v1/route_user.py` -> `create_user`: remove `current_user` parameter and comment `is_super_user` block
  - `app/db/repository/user.py` -> `create_new_user`: comment `available_models`
  - `app/schemas/user.py` -> comment all lines related to `available_models`

- Create initial docker images by running `docker-compose -f run_locally/docker-compose.dev.yml up --build`

  - `--build` flag ensures that Docker will rebuild the images specified in the Dockerfile if they are out of date or if there have been any changes to the Dockerfile or the files it copies into the container.
  - Docker will first build the application image by following the steps in the `Dockerfile`.
  - `nginx.conf` file should be in `run_locally` folder to run nginx
  - execute all commands inside YAML file
  - `localhost:8080` will be reachable

- Create a superuser via Swagger UI in `localhost:8080/docs`

### 4. Upgrade User table

- Stop all containers and remove them by running `docker stop $(docker ps -q)` and `docker rm $(docker ps -aq)`
- Run PostgreSQL, DynamoDB, Reddis by running `docker-compose -f run_locally/docker-compose.dbs.yml up -d`

  `-f` flag specifies the path to the Docker Compose YAML file, `-d`: This flag runs the containers in detached mode, meaning the command will run in the background

- Connect to postgreSQL database server via GUI (DBeaver or Other) by using credentials provided in `docker-compose.dbs.yml` file

  - Check if `available_columns` are not added in `user` table at this time

- Upgrade your database schema by running `alembic upgrade head` to the latest version as defined by your migration scripts

  - All versions defined in `alembic/versions` folder will be executed sequentially
  - `alembic.ini` should exist inside project root folder

- Check `user` table if `available_models` is added

### 5. Revert commented files to original

- Uncomment all source code in Section 2

### 6. Initialize dynamoDB

- `./run_locally/init-local-ddb.sh`
- `aws dynamodb list-tables --endpoint-url http://localhost:8000 --profile local` will list all tables in dynamodb
- Manually accessible to local dynamodb server by configuring provided in `.env` file on AWS NoSQL Workbench GUI
- `openai-call-log` table should be found

### 7. Two options to run Smart Owl locally

- `RUN_LOCALLY=true uvicorn app.main:app --host "localhost" --port 8080 --reload`
- `docker-compose -f run_locally/docker-compose.dev.yml up --build --scale api=2`

Run `localhost:8080`
