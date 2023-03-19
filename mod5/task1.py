import os
import shlex
import subprocess
import signal
from flask import Flask

app = Flask(__name__)

def open_port(port: int):
    command_str = f'lsof -i :{port}'
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True)
    result_list = result.stdout.decode().split('\n')[1:-1]
    busy_ports = []
    for item in result_list:
        busy_ports.append(int(item.split()[1]))

    if not os.getpid() in busy_ports:
        for pid in busy_ports:
            os.kill(pid, signal.SIGKILL)


if __name__ == "__main__":
    port = 5000
    open_port(port)
    app.run(port=port)