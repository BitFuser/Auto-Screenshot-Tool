import os
import sys
import subprocess
import time
import threading
from datetime import datetime

# === Auto-install dependencies if missing ===
RESTART_ENV_VAR = "AUTO_SCREENSHOT_RESTARTED"

def ensure_dependencies():
    try:
        from PIL import Image
        from mss import mss
        import tkinter as tk
        from tkinter import messagebox
    except ImportError:
        print("[INFO] Missing dependencies. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "mss", "pillow"])
        os.environ[RESTART_ENV_VAR] = "1"
        print("[INFO] Restarting script after installing dependencies...")
        os.execv(sys.executable, [sys.executable] + sys.argv)

# Avoid infinite loop
if not os.environ.get(RESTART_ENV_VAR):
    ensure_dependencies()

# === Safe to import now ===
from PIL import Image
from mss import mss
import tkinter as tk
from tkinter import messagebox

# === Auto Screenshot App ===
class AutoScreenshotApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Auto Screenshot Tool")
        self.master.geometry("300x220")
        self.master.resizable(False, False)

        self.running = False
        self.counter = 0

        tk.Label(master, text="Interval (seconds):").pack(pady=10)
        self.interval_entry = tk.Entry(master, justify="center")
        self.interval_entry.pack()
        self.interval_entry.insert(0, "5")

        tk.Button(master, text="Start", command=self.start).pack(pady=5)
        tk.Button(master, text="Stop", command=self.stop).pack(pady=5)

        self.status = tk.Label(master, text="Screenshots Taken: 0")
        self.status.pack(pady=10)

        self.folder = self.create_output_folder()

    def create_output_folder(self):
        # Save folder next to the script file
        script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        folder_name = "AutoScreenshots_" + datetime.now().strftime("%Y%m%d_%H%M%S")
        path = os.path.join(script_dir, folder_name)
        try:
            os.makedirs(path, exist_ok=True)
        except Exception as e:
            messagebox.showerror("Folder Error", f"Could not create folder:\n{e}")
            sys.exit(1)

        print(f"[INFO] Saving screenshots to: {path}")
        return path

    def take_screenshots(self):
        with mss() as sct:
            while self.running:
                screenshot = sct.grab(sct.monitors[1])
                img = Image.frombytes("RGB", (screenshot.width, screenshot.height), screenshot.rgb)
                filename = os.path.join(self.folder, f"screenshot_{datetime.now().strftime('%H%M%S')}.png")
                img.save(filename)
                self.counter += 1
                self.status.config(text=f"Screenshots Taken: {self.counter}")
                time.sleep(self.interval)

    def start(self):
        try:
            self.interval = float(self.interval_entry.get())
            if self.interval <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a positive number.")
            return

        if not self.running:
            self.running = True
            threading.Thread(target=self.take_screenshots, daemon=True).start()

    def stop(self):
        self.running = False

# === Run App ===
if __name__ == "__main__":
    root = tk.Tk()
    app = AutoScreenshotApp(root)
    root.mainloop()
