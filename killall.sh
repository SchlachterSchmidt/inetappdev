docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker volume rm workspace_pgdata
