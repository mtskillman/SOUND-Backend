from flask_cors import CORS
from flask import Flask
from auth_attempts_blueprints import attempt_blueprint
app = Flask(__name__)
app.register_blueprint(attempt_blueprint)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, support_credentials=True, resources={r"/": {"origins": "*"}})
if __name__ == '__main__':  # two environment vars: 'global_secret' and 'connection_url'
    app.run()
