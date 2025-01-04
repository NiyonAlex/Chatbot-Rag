docker-compose -f run_locally/docker-compose.dev.yml up --build

docker-compose -f run_locally/docker-compose.dbs.yml up -d

RUN_LOCALLY=true uvicorn app.main:app --host "localhost" --port 8080 --reload

docker stop $(docker ps -q)

docker rm $(docker ps -aq)