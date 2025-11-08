# Auto-Scaling in Web Applications in Cloud

This project implements a basic auto-scaling system for web applications, mirroring cloud services like AWS Auto Scaling or Alibaba Cloud by adjusting Flask instance counts based on CPU load to handle varying traffic efficiently.  Designed for local development on constrained hardware, it provides hands-on learning for scaling concepts before cloud deployment, including a dashboard for real-time metrics and a load simulator for testing.

## Features
- **Dynamic Instance Scaling**: Monitors system CPU and scales Flask instances from 1 to 5 when usage exceeds 35% (upscale) or falls below 15% (downscale), emulating cloud horizontal scaling.
- **Monitoring Dashboard**: Real-time terminal display of CPU, active instances, ports/PIDs, and requests per minute (RPM) calculated from app endpoints.
- **Live Visualization**: Matplotlib graph animates CPU usage and instance count over time for performance analysis.
- **Load Generation**: Configurable multi-threaded HTTP request sender to simulate traffic bursts, targeting the app or balancer.
- **Process Management**: Handles subprocesses for Flask instances with easy start/stop and listing via an AppManager class.
- **Load Balancer Stub**: Basic Flask entry point on port 8000, ready for extension to round-robin or least-connections routing across instances.

## Benefits in Cloud Context
Auto-scaling ensures cost savings by provisioning resources only as needed, improves availability during peaks, and maintains low latency for users, directly applicable to deploying this prototype on EC2 Auto Scaling Groups with Elastic Load Balancing.

## Installation
Clone the repo and set up the Python environment with the listed dependencies.

```bash
git clone https://github.com/kashbix/Auto-Scaling-in-Web-Application-in-Cloud.git
cd Auto-Scaling-in-Web-Application-in-Cloud
pip install -r requirements.txt
```

Key dependencies: Flask (web framework), psutil (system metrics), requests (HTTP client), matplotlib (plotting).

## Quick Start
Launch the scaler to initialize one Flask instance on port 5000 and begin auto-scaling monitoring.

```bash
python scaler.py
```

- The terminal dashboard will refresh every 3 seconds, showing active instances (e.g., `🟢 http://127.0.0.1:5000 (PID: 1234)`).
- A graph window opens for live CPU and instance tracking; close with Ctrl+C to stop.

Test scaling by generating load in a separate terminal.[16]

```bash
python load_generator.py --threads 20 --url http://127.0.0.1:5000/ --duration 300
```

For the load balancer (extend for full functionality):

```bash
python load_balancer.py --port 8000
```

Target it with load: `python load_generator.py --url http://127.0.0.1:8000/`.

Standalone app instance:

```bash
python app.py --port 5001
```

Each app handles requests with simulated CPU load and exposes `/requests` for count querying.

## Project Structure
```
.
├── app.py                 # Core Flask app with CPU simulation and metrics
├── scaler.py              # Auto-scaler, dashboard, and graphing logic
├── load_generator.py      # Traffic simulation tool
├── load_balancer.py       # Basic balancer (TODO: implement distribution)
├── process_manager.py     # Instance lifecycle management
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Limitations and Next Steps
This local setup uses global CPU for scaling, which may not capture app-specific loads—ideal for learning but extend with per-instance metrics for cloud accuracy.  The balancer is a stub; add routing logic for true distribution.  For cloud migration: Containerize with Docker, deploy to Kubernetes/AWS, and use Prometheus for advanced monitoring.  See open issues for enhancements like async tasks or ML-based scaling predictions.

## Contributing
Contributions welcome! Fork the repo, create a feature branch (`git checkout -b feature/amazing-feature`), commit changes (`git commit -m 'Add amazing feature'`), and open a pull request.  Focus areas: Improve balancer, add tests, or integrate cloud APIs—aligning with interests in cybersecurity and efficient local solutions.

## License
Distributed under the MIT License. See LICENSE for more information.
