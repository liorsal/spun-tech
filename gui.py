import tkinter as tk
import threading
import webbrowser
from app import app  # ייבוא האפליקציה מ-app.py

# פונקציה להפעלת השרת
def run_server():
    app.run(port=5000)

# פונקציה לפתיחת הדפדפן
def open_browser():
    webbrowser.open("http://localhost:5000")

# פונקציה שמתחילה את האפליקציה
def start_app():
    threading.Thread(target=run_server).start()
    threading.Timer(1, open_browser).start()

# יצירת חלון Tkinter
root = tk.Tk()
root.title("My App")

# כפתור להתחלת השרת
start_button = tk.Button(root, text="Start Server", command=start_app)
start_button.pack(pady=20)

# הפעלת הלולאה הראשית של Tkinter
root.mainloop()