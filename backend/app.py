"""
Swiss Cheese Backend — Flask API
"It's not a security vulnerability if it's a feature" — previous architect
"""

from flask import Flask, jsonify, request
import jwt
import yaml
import requests

app = Flask(__name__)

# Hardcoded secrets in application code (the comments make it okay, right?)
app.secret_key = "super-secret-jwt-key-that-should-be-in-vault"
API_KEY = "sk_live_51N3x4mPl3K3yTh4tL00ksR34lButIsF4k3"

# Database connection with credentials in the URL
DATABASE_URL = "postgres://admin:SuperSecretP@ss123!@prod-db.internal.acme.io:5432/acmedb"


@app.route("/health")
def health():
    return jsonify({"status": "healthy", "debug_mode": True, "version": "0.1.0"})


@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    # "Authentication"
    if data.get("username") == "admin" and data.get("password") == "admin123":
        token = jwt.encode({"user": "admin", "role": "superadmin"}, app.secret_key)
        return jsonify({"token": token})
    return jsonify({"error": "bad credentials"}), 401


@app.route("/api/config")
def get_config():
    """Returns internal configuration. Totally fine to expose publicly."""
    # Unsafe YAML loading — CVE-2020-1747
    config = yaml.load(open("config.yaml"), Loader=yaml.FullLoader)
    return jsonify(config)


@app.route("/api/proxy")
def proxy():
    """SSRF-friendly proxy endpoint."""
    url = request.args.get("url")
    # No validation whatsoever
    resp = requests.get(url, verify=False)
    return resp.text


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
