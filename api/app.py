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
    print("Received a request to the index route.")
    return "Hello, World!"

@app.route('/api', methods=['GET'])
def get_info():
    slack_name_param = request.args.get('slack_name', slack_name)
    track_param = request.args.get('track', track)
    
    if slack_name_param is None:
        return jsonify({"error": "slack_name parameter is missing"}), 400
    if track_param is None:
        return jsonify({"error": "track parameter is missing"}), 400
        
    current_day = datetime.datetime.now().strftime('%A')
    utc_time = datetime.datetime.now(pytz.UTC)
    utc_time_str = utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Status Code of Success (HTTP 200)
    status_code = 200

    # JSON response
    response_data = {
        "slack_name": slack_name_param,
        "current_day": current_day,
        "utc_time": utc_time_str,
        "track": track_param,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": status_code
    }

    return jsonify(response_data)

if __name__ == "__main__":
    print("Starting the Flask application...")
    app.run(debug=True)

