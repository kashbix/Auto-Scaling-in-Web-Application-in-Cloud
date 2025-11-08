from flask import Flask, redirect
import argparse

app = Flask(__name__)

# Simulate round-robin or single target
TARGET_PORT = 5000

@app.route('/')
def home():
    return f"Request handled by instance at port {TARGET_PORT}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8000)
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.port)
