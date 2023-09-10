#!/usr/bin/env python
from flask import Flask, jsonify, request, make_response
import datetime
import pytz

app = Flask(__name__)
app.json_sort_keys = False

slack_name = "Tipsy0"
github_repo_url = "https://github.com/tipsyx/app1.git"
github_file_url = "https://github.com/tipsyx/app1/blob/main/api/app.py"
track = "backend"

@app.route('/')
def index():
    response = make_response("", 200)
    return response

@app.route('/api/info', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name', slack_name)
    track = request.args.get('track', track)
    current_day = datetime.datetime.now().strftime('%A')
    utc_time = datetime.datetime.now(pytz.UTC)
    utc_time_str = utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Status Code of Success (HTTP 200)
    status_code = 200

    # JSON response
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time_str,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": status_code
    }

    return jsonify(response_data)

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple('localhost', 5000, app, use_reloader=True)
