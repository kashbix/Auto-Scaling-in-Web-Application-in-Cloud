from flask import Flask, request
import os

app = Flask(__name__)
request_count = 0

@app.route('/')
def home():
    global request_count
    request_count += 1
    # Simulate CPU load
    [x**2 for x in range(1000000)]
    return f"""
    <h2>Flask Instance Info</h2>
    <p>PID: {os.getpid()}</p>
    <p>Port: {request.environ.get('SERVER_PORT')}</p>
    <p>Requests handled: {request_count}</p>
    """

@app.route('/requests')
def get_requests():
    return str(request_count)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5000)
    args = parser.parse_args()

    # Bind to all interfaces, allow multiple requests, enable debug for auto reload
    app.run(host='0.0.0.0', port=args.port, threaded=True, debug=False)
