from flask import Flask
import subprocess
from datetime import datetime
import pytz
import os

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Replace with your full name
    name = "K K Subiksha"

    # Try to get the system username, use "unknown" if it fails
    username = os.getenv("USER") or os.getenv("USERNAME") or "unknown"

    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z%z')

    # Attempt to get `top` command output
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = f"Error retrieving top output: {e}"

    # Format the output in HTML
    html_output = f"<h1>System Information</h1>"
    html_output += f"<p><strong>Name:</strong> {name}</p>"
    html_output += f"<p><strong>Username:</strong> {username}</p>"
    html_output += f"<p><strong>Server Time (IST):</strong> {server_time}</p>"
    html_output += f"<pre>{top_output}</pre>"

    return html_output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
