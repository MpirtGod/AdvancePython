import os
import shlex
import subprocess
import signal
import time
from flask import Flask

app = Flask(__name__)

def try_open_port(port: int):
    command_str = f'lsof -i :{port}'
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True)
    result_list = result.stdout.decode().split('\n')[1:-1]
    busy_ports_pids = []
    for item in result_list:
        busy_ports_pids.append(int(item.split()[1]))

    if not os.getpid() in busy_ports_pids:
        for pid in busy_ports_pids:
            os.kill(pid, signal.SIGKILL)
    time.sleep(0.01)    #Без этой строчки выходит ошибка Port 5000 is in use by another program. Either identify and stop that program, or start the server with a different port.

if __name__ == "__main__":
    port = 5000
    try_open_port(port)
    app.run(port=port)