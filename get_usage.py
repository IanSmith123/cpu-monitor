import psutil
def cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent