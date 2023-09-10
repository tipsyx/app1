#!/usr/bin/env python
from flask import Flask, jsonify, request, make_response
import datetime
import pytz
import os

app = Flask(__name__)
app.json_sort_keys = False

app.secret_key = os.getenv("secret_key")
slack_name = os.getenv("slack_name")
github_repo_url = os.getenv("github_repo_url")
github_file_url = os.getenv("github_file_url")
track = os.getenv("track")

@app.route('/')
def index():
    print("Received a request to the index route.")
    return "Hello, World!"
    
@app.route("/api", methods=["GET"])
def retrieve():
    if request.method == "POST":
        return "<h1>Out of Bound</h1>", 400
    else:
        name = request.args.get('slack_name')
        trck = request.args.get('track')
       
        if name is not None and trck is not None:
            if name == slack_name and trck == track:
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
            else:
                return "Fatal error; Wrong Credentials", 401
        else:
            return "Error; missing a vital credential", 400

if __name__ == "__main__":
    print("Starting the Flask application...")
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))


