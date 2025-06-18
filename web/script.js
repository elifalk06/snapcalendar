const scheduleInput = document.getElementById('scheduleInput');
const processButton = document.getElementById('processButton');
const eventsList = document.getElementById('eventsList');
const remindersInput = document.getElementById('remindersInput');
const savePrefsButton = document.getElementById('savePrefs');

let reminders = {};

function loadPrefs() {
    const stored = localStorage.getItem('reminders');
    if (stored) {
        reminders = JSON.parse(stored);
        remindersInput.value = Object.entries(reminders)
            .map(([cat, min]) => `${cat}:${min}`).join(',');
    }
}

function savePrefs() {
    reminders = {};
    remindersInput.value.split(',').forEach(pair => {
        const [cat, min] = pair.split(':');
        if (cat && min) {
            reminders[cat.trim()] = parseInt(min.trim(), 10) || 0;
        }
    });
    localStorage.setItem('reminders', JSON.stringify(reminders));
}

function parseSchedule(text) {
    const events = [];
    const lines = text.split(/\n/);
    lines.forEach(line => {
        const regex = /(\d{4}-\d{2}-\d{2})\s+(\d{1,2}:\d{2})\s+(\w+)\s+(.*)/;
        const m = line.match(regex);
        if (m) {
            const dt = new Date(`${m[1]}T${m[2]}`);
            events.push({ date: dt, category: m[3], description: m[4] });
        }
    });
    return events;
}

function renderEvents(events) {
    eventsList.innerHTML = '';
    events.forEach(ev => {
        const li = document.createElement('li');
        const minutes = reminders[ev.category] || 0;
        const remindAt = new Date(ev.date.getTime() - minutes * 60000);
        li.textContent = `${ev.date.toLocaleString()} [${ev.category}] - ${ev.description} (remind at ${remindAt.toLocaleString()})`;
        eventsList.appendChild(li);
    });
}

processButton.addEventListener('click', () => {
    const events = parseSchedule(scheduleInput.value);
    renderEvents(events);
});

savePrefsButton.addEventListener('click', () => {
    savePrefs();
    alert('Preferences saved');
});

loadPrefs();
