import os
import hashlib
import hmac
import time
import urllib.parse
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()  # Load bot token from the .env file

app = Flask(__name__)
CORS(app)  # Ensure that the API allows external requests

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Read bot token from the .env file
MAX_TIME_DIFF = 300  # 5 minutes to block outdated data

def validate_telegram_data(init_data: str) -> bool:
    """Validates the integrity of Telegram Mini App data."""
    
    print(f"[LOG] Received initData: {init_data}")  # Log received data

    data_dict = dict(urllib.parse.parse_qsl(init_data, keep_blank_values=True))
    print(f"[LOG] Parsed data: {data_dict}")  # Show how the data is parsed

    received_hash = data_dict.pop("hash", None)
    if not received_hash:
        print("[LOG] No hash received, validation failed.")
        return False

    data_check_string = "\n".join(f"{k}={v}" for k, v in sorted(data_dict.items()))
    print(f"[LOG] Data check string: {data_check_string}")

    secret_key = hmac.new(
        key="WebAppData".encode(),
        msg=BOT_TOKEN.encode(),
        digestmod=hashlib.sha256
    ).digest()

    computed_hash = hmac.new(
        key=secret_key,
        msg=data_check_string.encode(),
        digestmod=hashlib.sha256
    ).hexdigest()

    print(f"[LOG] Received hash: {received_hash}")
    print(f"[LOG] Computed hash: {computed_hash}")

    if computed_hash != received_hash:
        print("[LOG] Hash does not match, validation failed.")
        return False

    auth_date = int(data_dict.get("auth_date", 0))
    if time.time() - auth_date > MAX_TIME_DIFF:
        print("[LOG] Data is too old, validation failed.")
        return False

    print("[LOG] Validation successful!")
    return True

@app.route("/validate", methods=["POST"])
def validate():
    data = request.json
    print(f"[LOG] Received JSON payload: {data}")  # Log the incoming JSON

    if not data or "initData" not in data:
        print("[LOG] No initData received.")
        return jsonify({"error": "No initData received"}), 400

    is_valid = validate_telegram_data(data["initData"])
    print(f"[LOG] Validation result: {is_valid}")
    return jsonify({"valid": is_valid})

if __name__ == "__main__":
    print("[LOG] Server starting at http://0.0.0.0:5000")
    app.run(debug=True, host="0.0.0.0", port=5000)
