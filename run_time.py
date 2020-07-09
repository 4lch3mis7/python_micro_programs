import ctypes


kernel32 = ctypes.windll.kernel32
run_time = kernel32.GetTickCount()  # in milliseconds
run_time = run_time / 1000  # in seconds
run_time = run_time / 60   # in minutes

print(f"System is running since {run_time} minutes.")
