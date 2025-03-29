from flask import Flask, render_template, request, redirect
import json
from datetime import datetime
from weasyprint import HTML
import os
import time
import threading
import webbrowser
from pathlib import Path

app = Flask(__name__)

# קביעת נתיב לתיקייה על שולחן העבודה
desktop = Path.home() / "Desktop"
archive_path = desktop / "קבצים ישנים"

# יצירת התיקייה אם היא לא קיימת
if not archive_path.exists():
    archive_path.mkdir(parents=True)

@app.route("/", methods=["GET"])
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form.to_dict()
    today = datetime.now().strftime("%Y-%m-%d")
    json_path = f"data/today.json"
    archive_path = f"data/archive/{today}.json"
    
    if not os.path.exists('data/archive'):
        os.makedirs('data/archive')

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    with open(archive_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    create_pdf(data, today)
    return redirect("/")

def create_pdf(data, date_str):
    html = render_template("form.html", data=data)
    pdf = HTML(string=html).write_pdf()
    with open(archive_path / f"form_{date_str}.pdf", "wb") as f:
        f.write(pdf)
    print(f"Saved form_{date_str}.pdf")

def save_pdf():
    today = datetime.now().strftime("%Y-%m-%d")
    create_pdf({}, today)

def check_and_save():
    last_saved_date = None
    while True:
        current_date = datetime.now().date()
        if last_saved_date != current_date:
            save_pdf()
            last_saved_date = current_date
        time.sleep(60)  # Check every minute

@app.route("/archive", methods=["GET"])
def archive():
    files = os.listdir('data/archive')
    pdf_files = [f for f in files if f.endswith('.pdf')]
    return render_template("archive.html", files=pdf_files)

def open_browser():
    webbrowser.open("http://localhost:5000")

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run(port=5000, debug=False)