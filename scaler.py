import psutil
import time
import os
import threading
import requests
from process_manager import AppManager
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -------------------
# Configuration
# -------------------
BASE_PORT = 5000
MAX_INSTANCES = 5
CPU_UPPER_THRESHOLD = 35
CPU_LOWER_THRESHOLD = 15
REFRESH_INTERVAL = 3  # seconds

manager = AppManager()
manager.start_instance(BASE_PORT)

cpu_data = []
instance_data = []
time_data = []

start_time = time.time()

# -------------------
# Terminal dashboard
# -------------------
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_rpm():
    total_requests = 0
    for inst in manager.list_instances():
        try:
            r = requests.get(f"http://127.0.0.1:{inst['port']}/requests", timeout=0.5)
            total_requests += int(r.text)
        except:
            pass
    elapsed_minutes = max((time.time() - start_time)/60, 0.01)
    return int(total_requests / elapsed_minutes)

def print_dashboard(cpu, instances):
    rpm = get_rpm()
    clear_terminal()
    print("="*60)
    print("                AUTO SCALER STATUS                ")
    print("="*60)
    print(f"CPU Usage       : {cpu:.2f}%")
    print(f"Active Instances: {len(instances)}")
    print("\nInstances:")
    for inst in instances:
        print(f"🟢 http://127.0.0.1:{inst['port']}  (PID: {inst['pid']})")
    print(f"\nRPM: {rpm}")
    print("="*60)

# -------------------
# Auto-scaling logic
# -------------------
def autoscaler():
    while True:
        cpu = psutil.cpu_percent(interval=1)
        instances = manager.list_instances()
        current_instances = len(instances)

        # Auto-scale logic
        if cpu > CPU_UPPER_THRESHOLD and current_instances < MAX_INSTANCES:
            next_port = BASE_PORT + current_instances
            manager.start_instance(next_port)
        elif cpu < CPU_LOWER_THRESHOLD and current_instances > 1:
            manager.stop_instance()

        # Update graph data
        cpu_data.append(cpu)
        instance_data.append(current_instances)
        time_data.append(time.time() - start_time)

        # Update dashboard
        print_dashboard(cpu, instances)

        time.sleep(REFRESH_INTERVAL)

# -------------------
# Matplotlib live graph
# -------------------
def run_graph():
    fig, ax = plt.subplots()
    line_cpu, = ax.plot([], [], label='CPU Usage (%)', color='red')
    line_instances, = ax.plot([], [], label='Active Instances', color='blue')

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("CPU / Instances")
    ax.set_title("Live CPU Usage & Active Instances")
    ax.legend()

    def update(frame):
        line_cpu.set_data(time_data, cpu_data)
        line_instances.set_data(time_data, instance_data)
        ax.relim()
        ax.autoscale_view()
        return line_cpu, line_instances

    ani = FuncAnimation(fig, update, interval=1000)
    plt.show()

# -------------------
# Run auto-scaler in a separate thread
# -------------------
threading.Thread(target=autoscaler, daemon=True).start()

# Run live graph (blocking)
run_graph()
