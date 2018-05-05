docker-compose -f docker-compose.yml -f docker-compose.dev.yml build

docker-compose up --scale app=4
