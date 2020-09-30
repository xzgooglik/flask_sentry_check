from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

app = Flask(__name__)

sentry_sdk.init(
    dsn="http://17efdce95ddy.your.company/3",
    integrations=[FlaskIntegration()])


@app.route("/")
def hello():
    return "Hello World from Flask"

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)

@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0
