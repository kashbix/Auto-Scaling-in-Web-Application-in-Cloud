import subprocess

class AppManager:
    def __init__(self):
        self.instances = []

    def start_instance(self, port):
        proc = subprocess.Popen(['python', 'app.py', f'--port={port}'])
        self.instances.append({'proc': proc, 'port': port, 'pid': proc.pid})
        print(f"🟢 Started Flask instance on port {port} | PID: {proc.pid}")

    def stop_instance(self):
        if self.instances:
            instance = self.instances.pop()
            instance['proc'].terminate()
            print(f"🔴 Stopped Flask instance on port {instance['port']} | PID: {instance['pid']}")

    def list_instances(self):
        return self.instances
