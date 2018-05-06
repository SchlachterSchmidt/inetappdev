docker exec workspace_app_1 python migrate.py db init
docker exec workspace_app_1 python migrate.py db migrate
docker exec workspace_app_1 python migrate.py db upgrade
