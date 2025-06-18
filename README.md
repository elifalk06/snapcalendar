# SnapCalendar

SnapCalendar is a simple Flask-based web application that lets you quickly turn
text descriptions of events into calendar entries. Type each event on a new
line and the app parses the text to detect dates and times.

You can also set specialized reminders for different categories in the **Preferences** page.

## Setup

Install dependencies and run the app:

```bash
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000` in your browser.

The main interface is rendered from **templates/index.html** and uses
**static/style.css** and **static/script.js** for styling and small client-side
enhancements.
