sudo docker-compose run --rm app bash
    > python migrate.py db init
    > python migrate.py db migrate
    > python migrate.py db upgrade