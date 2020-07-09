# CPU Usage Monitor
import psutil
import subprocess
import time

def per_cpu_usage():
    print("\nCPU Usage Per Core: ")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        print(f"Core {i}: {percentage}%")
        pass

# print(psutil.cpu_times())
def total_cpu_usage():
    total_cpu = psutil.cpu_percent(interval=None, percpu=False)
    return total_cpu




if __name__ == '__main__':   
    while True:
        print(per_cpu_usage())
        print(f"\nTotal CPU Usage: {total_cpu_usage()}% ", end='')
        time.sleep(0.8)
        try:
            subprocess.call('clear')
        except:
            subprocess.call('cls')











