import subprocess


def process_count(username: str) -> int:
    output = subprocess.check_output(["ps", "-u", username, "-o", "pid="])
    return len(output.splitlines())


def total_memory_usage(root_pid: int) -> float:
    output = subprocess.check_output(["ps", "--ppid", str(root_pid), "-o", "rss="])
    memory_usage = sum(map(int, output.splitlines()))
    output = subprocess.check_output(["ps", "-p", str(root_pid), "-o", "rss="])
    memory_usage += int(output.splitlines()[1])
    output = subprocess.check_output(["ps", "--ppid", str(root_pid), "-o", "pid="])
    child_pids = list(map(int, output.splitlines()))
    for pid in child_pids:
        output = subprocess.check_output(["ps", "-p", str(pid), "-o", "rss="])
        memory_usage += int(output.splitlines()[1])
    output = subprocess.check_output(["free", "-m"])
    total_memory = int(output.splitlines()[1].split()[1])
    return (memory_usage / total_memory) * 100