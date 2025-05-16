# 📸 Auto Screenshot Tool (with GUI)

This Python app captures **automatic screenshots** of your primary screen at a user-defined interval using a **simple GUI**. Screenshots are saved in a timestamped folder, and all dependencies install automatically on first run.

---

## 🧰 Features

- 🖼️ Simple Tkinter GUI
- ⏱️ Set custom time intervals (in seconds)
- 💾 Screenshots saved as `.png` in a new timestamped folder
- 🔁 Auto-installs `Pillow` and `mss` if missing
- 🚫 Handles bad input with user-friendly error dialogs

---

## 📦 Requirements

No manual installation needed!  
The script automatically installs missing dependencies on first run:

```bash
pip install pillow mss
```

---

## 🚀 How to Use

1. Run the script:
   ```bash
   python auto_screenshot_tool.py
   ```

2. Enter the desired screenshot **interval (in seconds)**.

3. Click **Start** to begin automatic screenshots.

4. Click **Stop** to end the session.

Screenshots will be saved to a folder named like:
```bash
AutoScreenshots_20250516_142203/
```

---

## 🖼️ GUI Preview

```text
+----------------------------+
|   Auto Screenshot Tool    |
+----------------------------+
| Interval (seconds): [ 5 ] |
| [ Start ]   [ Stop ]      |
| Screenshots Taken: 0      |
+----------------------------+
```

---

## 🛡️ Built-in Safety

- ✔ Prevents invalid inputs (e.g., zero or negative intervals)
- ✔ Auto-restarts after dependency installation
- ✔ Each session has a unique folder
- ✔ Uses daemon thread to keep GUI responsive

---

## 🧠 Tech Stack

- `tkinter` – GUI
- `mss` – Fast, cross-platform screen capture
- `Pillow` – Image processing
- `threading` – To avoid blocking the GUI
