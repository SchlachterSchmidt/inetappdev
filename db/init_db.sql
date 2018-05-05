CREATE USER app_user WITH LOGIN PASSWORD 'app_user';
ALTER ROLE app_user CREATEDB;

CREATE DATABASE dev_db;
CREATE DATABASE prd_db;

GRANT ALL PRIVILEGES ON DATABASE dev_db TO app_user;
GRANT ALL PRIVILEGES ON DATABASE prd_db TO app_user;
