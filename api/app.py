from flask import Flask, request, jsonify
import datetime
import pytz

app = Flask(__name__)

@app.route('/api/info', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name', 'Tipsy0')
    track = request.args.get('track', 'backend')
    current_day = datetime.datetime.now().strftime('%A')
    utc_time = datetime.datetime.now(pytz.UTC)
    utc_time_str = utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    github_repo_url = "https://github.com/tipsyx/app1.git"
    github_file_url = "https://github.com/tipsyx/app1/blob/main/api/app.py"
    
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

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
