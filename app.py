import tkinter as tk
import psutil
import time
import threading

def monitor_system(interval=5):
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()

        # Update the labels with the current system information
        cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
        memory_label.config(text=f"Memory Usage: {memory_info.percent}%")

        time.sleep(interval)

# Function to start monitoring in a separate thread
def start_monitoring():
    monitor_thread = threading.Thread(target=monitor_system, args=(5,))
    monitor_thread.daemon = True  # Daemonize thread so it exits when the program exits
    monitor_thread.start()

# Setting up the GUI
root = tk.Tk()
root.title("System Monitor")

# Create and place the labels for CPU and Memory usage
cpu_label = tk.Label(root, text="CPU Usage: ", font=("Helvetica", 16))
cpu_label.pack(pady=10)

memory_label = tk.Label(root, text="Memory Usage: ", font=("Helvetica", 16))
memory_label.pack(pady=10)

# Start monitoring when the GUI is ready
start_monitoring()

# Run the tkinter event loop
root.mainloop()
