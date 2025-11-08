# Auto-Scaling-in-Web-Application-in-Cloud

A local auto-scaling system for Flask applications that dynamically manages instances based on CPU usage thresholds, complete with monitoring dashboard, load generation, and visualization for educational purposes.

## Features
- **Dynamic Scaling**: Automatically starts or stops Flask instances (up to 5) when CPU exceeds 35% (scale up) or drops below 15% (scale down).
- **Real-Time Monitoring**: Terminal dashboard displays CPU usage, active instances, and requests per minute (RPM); live Matplotlib graph tracks metrics over time.
- **Load Simulation**: Multi-threaded request generator to test scaling under configurable traffic loads.
- **Instance Management**: Subprocess handling for Flask apps with PID and port tracking.
- **Basic Load Balancing Stub**: Flask-based balancer (extendable for round-robin distribution).

## Installation
Clone the repository and install dependencies via pip.

```bash
git clone https://github.com/kashbix/Auto-Scaling-in-Web-Application-in-Cloud
cd flask-auto-scaler
pip install -r requirements.txt
```

Requirements include Flask for the web app, psutil for CPU monitoring, requests for HTTP calls, and matplotlib for graphing.[15]

## Usage
Run the scaler to start the system with one initial instance on port 5000; it will auto-scale as needed.[16][11]

```bash
python scaler.py
```

- **View Dashboard**: Terminal refreshes every 3 seconds showing instances like `http://127.0.0.1:5000` and metrics.
- **Generate Load**: In a new terminal, simulate traffic targeting the balancer or app.

```bash
python load_generator.py --threads 20 --url http://127.0.0.1:8000/ --duration 120
```

- **Run Balancer**: Start separately if needed (currently static; extend for distribution).

```bash
python load_balancer.py --port 8000
```

- **Custom App Instance**: Launch standalone Flask apps on specific ports.

```bash
python app.py --port 5001
```

The graph window will open for live visualization; use Ctrl+C to stop.

## Project Structure
- `app.py`: Core Flask application with CPU-intensive endpoint and request counter
- `scaler.py`: Main autoscaler with monitoring and graphing logic.
- `load_generator.py`: Tool for simulating concurrent requests.
- `load_balancer.py`: Basic entry point (TODO: implement routing).
- `process_manager.py`: Manages subprocess instances.
- `requirements.txt`: Dependencies list.

## Limitations and Improvements
This is a prototype for local learning; global CPU scaling may not suit all loads—consider per-instance metrics.  Extend the balancer for true distribution and add logging/health checks for robustness.  For production, integrate Gunicorn and Docker; see issues for enhancements.

## Contributing
Fork the repo, create a branch, make changes, and submit a pull request.  Report bugs or suggest features via issues; all contributions welcome, especially for your interests in cybersecurity and ML integration.

## License
MIT License—feel free to use and modify.

[10](https://www.reddit.com/r/flask/comments/1ekjvap/i_made_a_quickstart_template_for_flask_apps/)
[11](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/58283121/80626aa3-fbf1-4593-807f-78a3cbf7f90a/scaler.py)
[12](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/58283121/8d08231b-61a5-49fc-9d0f-ec32f76fcc36/load_generator.py)
[13](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/58283121/3716dd8b-1df4-4134-86ec-117b95e96cbe/process_manager.py)
[14](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/58283121/ee67f335-68d0-4984-9669-99058cfdcda9/load_balancer.py)
[15](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/58283121/5c96dcef-4cf4-4026-98c1-35632c830d02/requirements.txt)
[16](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/58283121/a6414c1a-6943-4dc6-8946-759af1ee6989/app.py)
