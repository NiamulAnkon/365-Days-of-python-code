from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from routes import tasks_bp

app.register_blueprint(tasks_bp, url_prefix='/tasks')

if __name__ == '__main__':
    app.run(debug=True)
