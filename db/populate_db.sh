docker cp db/populate_db.sql workspace_db_1:/docker-entrypoint-initdb.d/populate.sql
docker exec -u postgres workspace_db_1 psql dev_db  -f docker-entrypoint-initdb.d/populate.sql
