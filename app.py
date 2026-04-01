from flask import Flask
from config import SECRET_KEY
from database.db import init_db
from routes.auth_routes import auth
from routes.user_routes import user


def create_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY

    app.register_blueprint(auth)
    app.register_blueprint(user)

    init_db()

    return app


def main():
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()