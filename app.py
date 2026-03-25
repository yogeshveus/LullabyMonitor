from flask import Flask
from config import SECRET_KEY
from database.db import init_db
from routes.auth_routes import auth
from routes.user_routes import user

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Register Blueprint
app.register_blueprint(auth)
app.register_blueprint(user)

# Initialize DB
init_db()

if __name__ == "__main__":
    app.run(debug=True)