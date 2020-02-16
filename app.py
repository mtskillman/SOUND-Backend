from flask import Flask
from auth_attempts_blueprints import attempt_blueprint

app = Flask(__name__)
app.register_blueprint(attempt_blueprint)


if __name__ == '__main__':  # two environment vars: 'global_secret' and 'connection_url'
    app.run()
