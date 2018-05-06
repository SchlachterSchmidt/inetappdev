"""Gunicorn entry point wrapping app creation."""

from app import create_app

app = create_app(config_mode='local')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000)