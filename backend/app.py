from flask import Flask, request, jsonify
from parser import parse_schedule
from scheduler import create_schedule
from emailer import send_weekly_email
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    # Extract class/exam dates and build a schedule
    dates = parse_schedule(path)
    schedule = create_schedule(dates, request.form)
    return jsonify(schedule)

@app.route('/send_email', methods=['POST'])
def email():
    user_email = request.json.get("email")
    message = request.json.get("message")
    send_weekly_email(user_email, message)
    return jsonify({"status": "email sent"})

if __name__ == '__main__':
    app.run(debug=True)
