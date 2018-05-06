docker exec workspace_app_1 python migrate_dev.py db init
docker exec workspace_app_1 python migrate_dev.py db migrate
docker exec workspace_app_1 python migrate_dev.py db upgrade
docker exec workspace_app_1 rm migrations
