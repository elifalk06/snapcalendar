# SnapCalendar

This project contains a very small prototype for a calendar web page. Users can
enter their schedule in a free-text box and have the events parsed into a list.
A preferences section lets users configure how many minutes in advance they want
reminders for certain categories of events.

## Usage

Open `web/index.html` in a browser. Type your events with one per line using the
format:

```
YYYY-MM-DD HH:MM category description
```

For example:

```
2024-06-10 08:00 school Math class
2024-06-10 17:30 soccer Practice at the field
```

Set reminder preferences in the form `category:minutes`. Multiple categories can
be separated by commas, e.g. `school:60,soccer:30`. When you press **Process
Schedule**, the events will be shown along with the time you will be reminded.

